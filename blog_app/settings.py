#!/usr/env/python
# -*- coding: utf-8 -*-

import os

environment = os.environ.get('ENVIRONMENT')
environemnt = environment.lower() if environment is not None else 'production'

SETTINGS = {
    'DEBUG': False,
    'TESTING': False,
    'SECRET_KEY': 'sample-secret-key',
    'SESSION_COOKIE_DOMAIN': 'diogoosorio.com',
    'SESSION_COOKIE_HTTPONLY': True,
    'SESSION_COOKIE_SECURE': False,
    'SERVER_NAME': 'diogoosorio.com',
    'INK_ASSET_MINIFY': True,
    'INK_ASSET_VERSION': '2.2.1',
    'INK_ASSET_DEFAULT_LOCATION': 'local',
    'ENVIRONMENT': environment,
}

CACHE_SETTINGS = {
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 25,
    'CACHE_KEY_PREFIX': 'diogoo_blog_',
    'CACHE_DIR': '/tmp/diogoosorio.com/cache'
}

GITHUB_SETTINGS = {
    'username': 'diogoosorio',
    'password': '{+4=ahe[oYi\IJ!C//Ij/LZdN',
    'repository': 'diogosorio/blog-entries'
}

if environment == 'development':
    SETTINGS['DEBUG'] = True
    SETTINGS['TESTING'] = True
    SETTINGS['SESSION_COOKIE_DOMAIN'] = None,
    SETTINGS['SERVER_NAME'] = None
    SETTINGS['HOST'] = '0.0.0.0'
    SETTINGS['INK_ASSET_MINIFY'] = False

    CACHE_SETTINGS['CACHE_TYPE'] = 'null'
