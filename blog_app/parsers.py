#!/usr/env/python
# -*- coding: utf-8 -*-

import BeautifulSoup
import misaka as m
import re
import datetime

class BaseParser(object):

    EXCERPT_MAX_LENGTH = 600

    def extrafilemeta(self, filepath):
        with file(filepath) as f:
            content = f.read().decode('utf-8')

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
            if key == 'create_date':
                val = datetime.datetime.strptime(val.strip(), '%Y-%m-%d').date()

            final_meta[key] = val

        content = self.parse(content)
        final_meta['excerpt'] = self.make_excerpt(content)

        return [final_meta, content]

    def make_excerpt(self, content):
        no_html = BeautifulSoup.BeautifulSoup(content).findAll(text=True)
        no_html = no_html[0:self.EXCERPT_MAX_LENGTH]
        return no_html



class MisakaWrapper(BaseParser):
    def parse(self, text):
        return m.html(text)
