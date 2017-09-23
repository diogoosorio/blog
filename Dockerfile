FROM python:3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && \
    apt-get install -y build-essential libmemcached-dev && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

EXPOSE 4000

CMD uwsgi --ini blog_app.ini
