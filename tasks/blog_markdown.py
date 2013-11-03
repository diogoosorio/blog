#!/usr/env/python
# -*- coding: utf-8 -*-

from __future__ import division
from datetime import date
import pymongo
import math
import html2text
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENTRIES_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir, 'entries'))

def entries():
    client = pymongo.MongoClient()
    coll = client.blog.blog
    return coll.find(spec={'status': '1'}, skip=0, limit=-1)

def extract_metadata(item):
    html_meta = item['seo'] if 'seo' in item and type(item['seo']) is dict else {}
    meta = {
        'create_date': date.fromtimestamp(item.get('added')),
        'title': html_meta.get('title'),
        'description': html_meta.get('description'),
        'keywords': html_meta.get('keywords'),
        'slug': item.get('slug'),
        'category': item.get('category')
    }
    return meta

def extract_content(item):
    h = html2text.HTML2Text()
    return h.handle(item.get('text'))

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

    meta_str = "\n".join([': '.join((k, str(meta[k]))) for k in meta])

    filename = meta['slug'].replace('-', '_')+'.md'
    file_content = "----\n%s\n----\n\n%s" % (meta_str, content)
    create_blogentry(filename, file_content)

    file_list[meta['create_date']] = filename

# Another passage to sort/rename tne entries
i = 1
for key in sorted(file_list.iterkeys()):
    filename = file_list[key]
    prefix = str(i).zfill(3)
    new_filename = prefix + "_" + filename
    rename_blogentry(filename, new_filename)
    i += 1
