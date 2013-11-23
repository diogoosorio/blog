#!/bin/bash

UWSGI_USER="uwsgi"
UWSGI_GROUP="uwsgi"
PID_FILE=uwsgi.pid
MAX_REQUESTS=50
WORKERS=1
SOCKET="127.0.0.1:8889"

# Check if the virtual environment is present
if [ ! -d "venv" ]; then
    virtualenv venv
    venv/bin/pip install -r requirements.txt
fi

# Check if uwsgi is present
if [ ! -f "venv/bin/uwsgi" ]; then
    venv/bin/pip install uwsgi
fi

# Find the uwsgi run user
UWSGI_UID=$(id -u $UWSGI_USER)
UWSGI_GID=$(id -g $UWSGI_GROUP)

venv/bin/uwsgi -s $SOCKET --master --module blog_app.blog_app --callable app \
    --workers $WORKERS --harakiri 30 --max-requests $MAX_REQUESTS --pidfile $PID_FILE \
    --uid $UWSGI_UID --gid $UWSGI_GID
