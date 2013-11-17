#!/usr/env/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, url_for, g, abort, request
from flask_ink.ink import Ink
from flask.ext.cache import Cache
from settings import SETTINGS, CACHE_SETTINGS
from repository import LocalRepository
from parsers import MisakaWrapper
from pagination import BlogPagination

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


@app.route('/')
def index():
    return redirect('/blog', 301)


@cache.cached(timeout=1200)
@app.route('/blog/')
def blog():
    page = request.args.get('page')
    page = int(page) if page is not None else 1

    template_variables = g.repository.getfiles('entries', page)
    template_variables['pagination'] = BlogPagination(page=page, total=template_variables['total'], per_page=app.config['PAGESIZE'])

    if not template_variables['entries']:
        abort(404)

    return render_template('blog.html', **template_variables)


@app.route('/blog/rss/')
@cache.cached(timeout=1200)
def rss():
    return 'RSS'


@cache.memoize(timeout=3600)
@app.route('/blog/<post_name>')
def blog_detail(post_name):
    return post_name


if __name__ == '__main__':
    Ink(app)

    app.jinja_env.globals.update(load_asset=load_asset)
    app.run(host=app.config['HOST'])
