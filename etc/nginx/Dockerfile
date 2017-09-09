FROM nginx:1.13

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests certbot && \
    rm -rf /var/lib/apt/lists/*
