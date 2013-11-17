#!/usr/env/python
# -*- coding: utf-8 -*-

import os, math

class LocalRepository(object):

    CACHE_GETFILES_TIMEOUT = 3600

    def __init__(self, base_dir, parser, cache = None, pagesize = 5):
        self.base_dir = os.path.abspath(base_dir)
        self.parser = parser
        self.cache = cache
        self.pagesize = pagesize

        self.testdir(self.base_dir)

    def getfile(self,directory, slug):
        cache_key = "file-detail-{}".format(slug)
        entry = self.cache.get(cache_key)

        if not entry:
            filename = slug + ".md"
            filepath = os.path.abspath(os.path.join(self.base_dir, directory, filename))

            if os.path.exists(filepath):
                meta, content = self.parser.extractfilemeta(filepath)
                entry = {'meta': meta, 'content': content}

        return entry


    def getfiles(self, directory, page):
        cache_key = "all-files-{}".format(directory)
        files = self.cache.get(cache_key)

        if not files:
            directory = os.path.abspath(os.path.join(self.base_dir, directory))
            self.testdir(directory)
            files = []

            for file in os.listdir(directory):
                meta, content = self.parser.extractfilemeta(os.path.join(directory, file))
                parsed_file = {'meta': meta, 'content': content}
                files.append(parsed_file)

            # Sort the file list by publish date
            files.sort(key=lambda x: x['meta']['create_date'], reverse=True)

        self.cache.set(cache_key, files, self.CACHE_GETFILES_TIMEOUT)
        sliced_files = self.paginate(files, page)
        response = {'total': len(files), 'entries': sliced_files}

        return response

    def paginate(self, files, page):
        limit = self.pagesize
        offset = (page - 1) * self.pagesize
        sliced_files = files[offset:(limit + offset)]

        return sliced_files


    def testdir(self, directory):
        if not os.path.exists(directory):
            raise RuntimeError("The repository path doesn't exist.")
