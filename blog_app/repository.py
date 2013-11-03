#!/usr/env/python
# -*- coding: utf-8 -*-

import os

class LocalRepository(object):
    def __init__(self, base_dir, parser):
        self.base_dir = os.path.abspath(base_dir)
        self.parser = parser
        self.testdir(self.base_dir)

    def getfiles(self, directory, limit=None, offset=0):
        directory = os.path.abspath(os.path.join(self.base_dir, directory))
        self.testdir(directory)

        dirfiles = sorted(os.listdir(directory), reverse=True)
        dirfiles = dirfiles[offset:limit] if type(limit) is int else dirfiles[offset:]

        for index, file in enumerate(dirfiles):
            meta, content = self.parser.extrafilemeta(os.path.join(directory, file))
            dirfiles[index] = {'meta': meta, 'content': content}

        return dirfiles


    def testdir(self, directory):
        if not os.path.exists(directory):
            raise RuntimeError("The repository path doesn't exist.")
