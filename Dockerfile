FROM python:3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get install -y build-essential libmemcached-dev && \
    pip install -r requirements.txt

COPY . /app

RUN mkdir -p /www/diogoosorio.com/logs/

EXPOSE 5000

CMD uwsgi --ini blog_app.ini
