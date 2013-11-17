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
            else:
                val = val.strip()

            final_meta[key] = val

        content = self.parse(content)
        final_meta['excerpt'] = self.make_excerpt(content)

        return [final_meta, content]

    def make_excerpt(self, content):
        soup = BeautifulSoup.BeautifulSoup(content)

        p = soup.p
        if p is None:
            return content

        excerpt = [p.renderContents()]
        next_sibling = None
        next_element = p

        while next_sibling is None:
            next_element = next_element.nextSibling

            # BeautifulSoup was returning newline characters as the next sibling,
            # we want to discard those...
            if not isinstance(next_element, BeautifulSoup.Tag):
                continue

            validtag = next_element.name.lower() == 'p'
            next_sibling = next_element if validtag else False

        if next_sibling:
            excerpt.append(next_sibling.renderContents())

        return "\n".join('<p>{0}</p>'.format(p) for p in excerpt)



class MisakaWrapper(BaseParser):
    def parse(self, text):
        return m.html(text)
