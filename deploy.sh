#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

eval "$(ssh-agent -s)"
echo "$SSH_DEPLOY_KEY" > /tmp/deploy_rsa
chmod 0600 /tmp/deploy_rsa
ssh-add /tmp/deploy_rsa

ssh $SSH_DEPLOY_USER@diogoosorio.com <<ENDSSH
  set -o errexit
  set -o pipefail
  set -o nounset

  docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"

  docker pull diogoosorio/blog:latest
  docker pull memcached:1.5
  
  docker stop diogoosorio_blog || true
  docker stop diogoosorio_memcached || true

  docker rm diogoosorio_blog || true
  docker rm diogoosorio_memcached || true

  docker run -d --name diogoosorio_memcached -d memcached:1.5
  docker run -d --name diogoosorio_blog \
    -d --link diogoosorio_memcached:memcached \
    -p 4000:4000 \
    diogoosorio/blog:latest

  docker cp diogoosorio_blog:/app/src/blog_app/static /var/www/diogoosorio.com
  docker system prune -f
ENDSSH
