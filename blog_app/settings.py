#!/usr/env/python
# -*- coding: utf-8 -*-

import os

environment = os.environ.get('ENVIRONMENT')
environemnt = environment.lower() if environment is not None else 'production'

SETTINGS = {
    'DEBUG': False,
    'TESTING': False,
    'SECRET_KEY': 'sample-secret-key',
    'HOST': '0.0.0.0',
    'SESSION_COOKIE_DOMAIN': 'diogoosorio.com',
    'SESSION_COOKIE_HTTPONLY': True,
    'SESSION_COOKIE_SECURE': False,
    'REPO_DIRECTORY': '/var/www/diogoosorio.com/content',
    'LOG_LOCATION': '/var/www/diogoosorio.com/logs/flask.log',
    'PAGESIZE': 5,
    'INK_ASSET_MINIFY': True,
    'INK_ASSET_VERSION': '2.2.1',
    'INK_ASSET_DEFAULT_LOCATION': 'local',
    'ENVIRONMENT': environment,
    'DISQUS_SHORTNAME': 'diogoosorio'
}

CACHE_SETTINGS = {
    'CACHE_TYPE': 'memcached',
    'CACHE_DEFAULT_TIMEOUT': 25,
    'CACHE_KEY_PREFIX': 'diogoo_blog_',
    'CACHE_DIR': '/tmp/diogoosorio.com/cache'
}

if environment == 'development':
    SETTINGS['DEBUG'] = True
    SETTINGS['TESTING'] = True
    SETTINGS['SESSION_COOKIE_DOMAIN'] = None,
    SETTINGS['SERVER_NAME'] = None
    SETTINGS['INK_ASSET_MINIFY'] = False
    SETTINGS['DISQUS_SHORTNAME'] = 'diogoosorio-blog-dev'
    SETTINGS['REPO_DIRECTORY'] = '/workspace/blog/content'
    SETTINGS['LOG_LOCATION'] = '/tmp/diogoosorio.com_flask.log'

    CACHE_SETTINGS['CACHE_TYPE'] = 'null'
