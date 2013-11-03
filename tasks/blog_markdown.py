#!/usr/env/python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import date
import pymongo
import math
import html2text
import os
import re

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir, 'content', 'entries'))

def entries():
    client = pymongo.MongoClient()
    coll = client.blog.blog
    return coll.find(spec={'status': '1'}, skip=0, limit=-1)

def extract_metadata(item):
    html_meta = item['seo'] if 'seo' in item and type(item['seo']) is dict else {}
    create_date = date.fromtimestamp(item.get('added'))

    h = html2text.HTML2Text()
    meta = {
        'create_date': create_date.isoformat(),
        'title': html_meta.get('title'),
        'description': html_meta.get('description'),
        'keywords': html_meta.get('keywords'),
        'slug': item.get('slug'),
        'category': item.get('category')
    }
    return meta

def extract_content(item):
    content = item.get('text')
    content = content.replace('&nbsp;', ' ')
    content = content.replace('../../public/images/blog/', '/static/images/blog/')

    h = html2text.HTML2Text()
    return h.handle(content)

def create_blogentry(filename, contents):
    absolute_filepath = os.path.join(ENTRIES_DIR, filename)
    with open(absolute_filepath, 'w') as f:
        f.write(contents.encode('utf8'))

def rename_blogentry(filename, newfilename):
    filepath = os.path.join(ENTRIES_DIR, filename)
    newfilepath = os.path.join(ENTRIES_DIR, newfilename)
    os.rename(filepath, newfilepath)

entries = entries()
file_list = {}

for i in range(0, (entries.count() - 1)):
    meta = extract_metadata(entries[i])
    content = extract_content(entries[i])

    meta_str = "\n".join([': '.join((k, meta[k])) for k in meta])

    filename = meta['slug']+'.md'
    file_content = "----\n%s\n----\n\n%s" % (meta_str, content)
    create_blogentry(filename, file_content)
