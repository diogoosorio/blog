#!/bin/bash

if [ ! -d "venv" ]; then
    virtualenv venv
    venv/bin/pip install -r requirements.txt
fi

if [ ! -f "venv/bin/uwsgi" ]; then
    venv/bin/pip install uwsgi
fi

venv/bin/uwsgi -s /tmp/diogoosorio.com.sock --module blog_app.blog_app --callable app
