from __future__ import unicode_literals

from django.contrib import admin

from import_export.admin import ImportExportMixin, ExportActionModelAdmin
from import_export import resources
from import_export import fields

from .models import Book, Category, Author


class BookResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name="Book name")

    class Meta:
        model = Book


class BookAdmin(ImportExportMixin, admin.ModelAdmin):
    list_filter = ['categories', 'author']
    resource_class = BookResource


class CategoryAdmin(ExportActionModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
