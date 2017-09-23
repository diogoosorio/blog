from flask_paginate import Pagination
from .parsers import Helper

class BlogPagination(Pagination):
    """
    Golden hammer. Overrides the links getter and appends Ink's pagination
    classes to the damn thing.

    TODO: Create a ink pagination class of its own and delete this...
    """

    @property
    def links(self):
        links = super().links
        soup = Helper.parse(links)
        soup.ul['class'] = "pagination black rounded shadowed separated push-right"
        return soup.renderContents().decode('utf-8')
