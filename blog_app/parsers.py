#!/usr/env/python
# -*- coding: utf-8 -*-

import misaka as m
import re

class BaseParser(object):
    def extrafilemeta(self, filepath):
        with file(filepath) as f:
            content = f.read()

        return self.extractmeta(content)

    def extractmeta(self, text):
        parts = re.split('-{4}', text)
        meta = parts[1].strip()
        content = "----".join(parts[2:]).strip()

        if not hasattr(self, 'meta_pattern'):
            self.meta_pattern = re.compile('([\w]+):(.+)', re.M)

        meta_matches = re.findall(self.meta_pattern, meta)
        final_meta = {}

        for key, val in meta_matches:
            final_meta[key] = val

        content = m.html(content)

        return [final_meta, content]


class MisakaWrapper(BaseParser):
    def parse(self, text):
        meta, text = self.extractmeta(text)
        print meta
