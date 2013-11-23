#!/bin/bash

UWSGI_USER="uwsgi"
UWSGI_GROUP="uwsgi"
PID_FILE=uwsgi.pid
MAX_REQUESTS=50
WORKERS=1
SOCKET="127.0.0.1:8889"
LOG_DIR="./logs"
DAEMONIZE_LOG=daemonize.log


function start(){

    if [ -f $PID_FILE ]; then
        echo "Cannot start uwsgi. PID file detected ($PID_FILE), please stop the process before starting it."
        exit -1
    fi

    # Check if the virtual environment is present
    if [ ! -d "venv" ]; then
        virtualenv venv
        venv/bin/pip install -r requirements.txt
    fi

    # Check if uwsgi is present
    if [ ! -f "venv/bin/uwsgi" ]; then
        venv/bin/pip install uwsgi
    fi

    # Add the log directory
    if [ ! -d $LOG_DIR ]; then
        mkdir $LOG_DIR
        chown -R $UWSGI_USER $LOG_DIR
        chgrp -R $UWSGI_GROUP $LOG_DIR
    fi

    # Find the uwsgi run user
    UWSGI_UID=$(id -u $UWSGI_USER)
    UWSGI_GID=$(id -g $UWSGI_GROUP)

    venv/bin/uwsgi -s $SOCKET --master --module blog_app.blog_app --callable app \
        --workers $WORKERS --harakiri 30 --max-requests $MAX_REQUESTS --pidfile $PID_FILE \
        --uid $UWSGI_UID --gid $UWSGI_GID --logto $LOG_DIR/uwsgi.log --daemonize $LOG_DIR/$DAEMONIZE_LOG
}

function stop(){
    if [ -f $PID_FILE ]; then
        while read pid; do
            echo "Killing $pid"
            kill -9 $pid
        done < $PID_FILE

        rm $PID_FILE
    else
        echo "No PID file found ($PID_FILE)"
    fi
}

function help(){
    echo "Usage: sh run.sh {start|stop}"
}

if [ $# -eq 0 ]; then
    help
elif [ "$1" == "start" ]; then
    start
elif [ "$1" == "stop" ]; then
    stop
else
    echo "Unknown command $1"
    help
fi
