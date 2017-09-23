import uuid
import re

from flask import Flask, redirect, render_template, g, abort, request, make_response
from flask_ink.ink import Ink
from flask_caching import Cache

from .settings import SETTINGS, CACHE_SETTINGS
from .repository import LocalRepository
from .parsers import BlogParser
from .pagination import BlogPagination


def build_app():
    _app = Flask(__name__)
    _app.config.update(SETTINGS)

    _cache = Cache(_app, config=CACHE_SETTINGS)

    Ink(_app)

    return [_app, _cache]


app, cache = build_app() # pylint: disable=invalid-name

@app.before_request
def before_request():
    content_dir = app.config['REPO_DIRECTORY']
    parser = BlogParser()
    g.repository = LocalRepository(content_dir, parser, cache, app.config['PAGESIZE'])

    # pagination
    page = request.args.get('page')
    page = int(page) if page is not None and page.isdigit() else 1
    g.page = page


@app.route('/')
def index():
    return redirect('/blog', 301)


@cache.cached(timeout=1200)
@app.route('/blog/')
def blog():
    template_variables = g.repository.getfiles('entries', g.page)
    template_variables['pagination'] = BlogPagination(
        page=g.page,
        total=template_variables['total'],
        per_page=app.config['PAGESIZE']
    )

    if not template_variables['entries']:
        abort(404)

    return render_template('blog.html', **template_variables)


@app.route('/blog/rss/')
@cache.cached(timeout=1200)
def rss():
    template_variables = g.repository.getfiles('entries', g.page)

    g.repository.pagesize = 1
    last_entry = g.repository.getfiles('entries', 1)
    last_entry = last_entry['entries'][0] if last_entry['entries'] else None

    template_variables['uuid'] = uuid
    template_variables['last_entry'] = last_entry

    response = make_response(render_template('atom.xml', **template_variables))
    response.headers['Content-Type'] = 'application/atom+xml'
    return response


@app.errorhandler(404)
def page_not_found():
    path = request.path
    legacy_match = re.match(r'^/blog/entry/([\w-]+)/?$', path, re.I)

    if legacy_match:
        slug = legacy_match.group(1)
        entry = g.repository.getfile('entries', slug)

        if entry:
            return redirect("/blog/{0}".format(slug), 301)

    return render_template('404.html', path=path), 404


@cache.memoize(timeout=3600)
@app.route(u'/blog/<post_name>')
def blog_detail(post_name):
    entry = g.repository.getfile('entries', post_name)

    if not entry:
        abort(404)

    template_variables = {
        'entry': entry,
        'title': entry['meta'].get('title'),
        'description': entry['meta'].get('description')
    }

    return render_template('detail.html', **template_variables)


if __name__ == '__main__':
    app.run(host=app.config['HOST'])
