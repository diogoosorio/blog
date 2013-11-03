#!/usr/env/python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, render_template, url_for
from flask_ink.ink import Ink
from flask.ext.cache import Cache
from settings import SETTINGS, CACHE_SETTINGS

app = Flask(__name__)
app.config.update(SETTINGS)

cache = Cache(app, CACHE_SETTINGS)

def load_asset(filename):
    environment = app.config['ENVIRONMENT']

    if environment != 'development':
        filename = '%s.min.%s' % tuple(filename.rsplit('.', 1))

    return url_for('static', filename=filename)


@app.route('/')
def index():
    return redirect('/blog', 301)

@cache.cached(timeout=1200)
@app.route('/blog/<int:page>/')
@app.route('/blog/')
def blog(page=1):
    return str(page)

@app.route('/blog/rss/')
@cache.cached(timeout=1200)
def rss():
    return 'RSS'

@cache.memoize(timeout=3600)
@app.route('/blog/entry/<post_name>')
def blog_detail(post_name):
    return post_name

if __name__ == '__main__':
    Ink(app)

    app.jinja_env.globals.update(load_asset=load_asset)
    app.run(host=SETTINGS['HOST'])
