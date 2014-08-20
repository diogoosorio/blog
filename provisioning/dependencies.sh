#!/bin/bash

apt-get update && apt-get dist-upgrade -y
apt-get install -y python python-dev python-setuptools build-essential
easy_install pip
pip install --upgrade pip
pip install --upgrade virtualenv
