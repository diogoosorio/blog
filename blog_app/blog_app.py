#!/usr/env/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, url_for, g, abort, request, make_response
from flask_ink.ink import Ink
from flask.ext.cache import Cache
from settings import SETTINGS, CACHE_SETTINGS
from repository import LocalRepository
from parsers import MisakaWrapper
from pagination import BlogPagination
import uuid

app = Flask(__name__)
app.config.update(SETTINGS)

cache = Cache(app, CACHE_SETTINGS)

def load_asset(filename):
    environment = app.config['ENVIRONMENT']

    if environment != 'development':
        filename = '%s.min.%s' % tuple(filename.rsplit('.', 1))

    return url_for('static', filename=filename)


@app.before_request
def before_request():
    content_dir = app.config['REPO_DIRECTORY']
    parser = MisakaWrapper()
    g.repository = LocalRepository(content_dir, parser, cache, app.config['PAGESIZE'])

    # pagination
    page = request.args.get('page')
    page = int(page) if page is not None else 1
    g.page = page


@app.route('/')
def index():
    return redirect('/blog', 301)


@cache.cached(timeout=1200)
@app.route('/blog/')
def blog():
    template_variables = g.repository.getfiles('entries', g.page)
    template_variables['pagination'] = BlogPagination(page=g.page, total=template_variables['total'], per_page=app.config['PAGESIZE'])

    if not template_variables['entries']:
        abort(404)

    return render_template('blog.html', **template_variables)


@app.route('/blog/rss/')
@cache.cached(timeout=1200)
def rss():
    template_variables = g.repository.getfiles('entries', g.page)

    g.repository.pagesize = 1
    last_entry = g.repository.getfiles('entries', 1)
    last_entry = last_entry['entries'][0] if len(last_entry['entries']) else None

    template_variables['uuid'] = uuid # TODO: This logic shouldn't be on the template...
    template_variables['last_entry'] = last_entry

    response = make_response(render_template('atom.xml', **template_variables))
    response.headers['Content-Type'] = 'application/atom+xml'
    return response


@cache.memoize(timeout=3600)
@app.route('/blog/<post_name>')
def blog_detail(post_name):
    entry = g.repository.getfile('entries', post_name)

    if not entry:
        abort(404)

    return render_template('detail.html', entry=entry)


if __name__ == '__main__':
    Ink(app)

    app.jinja_env.globals.update(load_asset=load_asset)
    app.run(host=app.config['HOST'])
