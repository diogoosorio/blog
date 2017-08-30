FROM python:3

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt && \
    python blog_app.py