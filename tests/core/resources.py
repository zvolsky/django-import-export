from __future__ import unicode_literals

from import_export.resources import ModelResource
from import_export import fields
from import_export.widgets import NumberWidget

from .models import Book


class BookResource(ModelResource):
    published = fields.Field(attribute='published',
                             widget=NumberWidget())

    class Meta:
        model = Book
