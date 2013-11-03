#!/usr/env/python
# -*- coding: utf-8 -*-

from github import Github

class GithubRepository(object):

    def __init__(self, configuration):
        self.username = configuration.get('username')
        self.password = configuration.get('password')
        self.repository = configuration.get('repository')
