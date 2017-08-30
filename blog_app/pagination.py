#!/usr/env/python
# -*- coding: utf-8 -*-

from flask_paginate import Pagination
from bs4 import BeautifulSoup

class BlogPagination(Pagination):
    """
    Golden hammer. Overrides the links getter and appends Ink's pagination
    classes to the damn thing.

    TODO: Create a ink pagination class of its own and delete this...
    """

    @property
    def links(self):
        links = Pagination.links.fget(self)
        soup = BeautifulSoup(links)
        soup.ul['class'] = "pagination black rounded shadowed separated push-right"
        return soup.renderContents()
