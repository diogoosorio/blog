#!/usr/env/python
# -*- coding: utf-8 -*-

import os

class LocalRepository(object):

    CACHE_GETFILES_TIMEOUT = 3600

    def __init__(self, base_dir, parser, cache = None):
        self.base_dir = os.path.abspath(base_dir)
        self.parser = parser
        self.cache = cache

        self.testdir(self.base_dir)

    def getfiles(self, directory, limit=None, offset=0):
        cache_key = "all-files-{}".format(directory)
        files = self.cache.get(cache_key)

        if not files:
            directory = os.path.abspath(os.path.join(self.base_dir, directory))
            self.testdir(directory)
            files = []

            for file in os.listdir(directory):
                meta, content = self.parser.extrafilemeta(os.path.join(directory, file))
                parsed_file = {'meta': meta, 'content': content}
                files.append(parsed_file)

            # Sort the file list by publish date
            files.sort(key=lambda x: x['meta']['create_date'], reverse=True)

        self.cache.set(cache_key, files, self.CACHE_GETFILES_TIMEOUT)
        sliced_files = files[offset:(limit + offset)] if type(limit) is int else files[offset:]
        response = {'total': len(files), 'limit': limit, 'offset': offset, 'entries': sliced_files}

        return response


    def testdir(self, directory):
        if not os.path.exists(directory):
            raise RuntimeError("The repository path doesn't exist.")
