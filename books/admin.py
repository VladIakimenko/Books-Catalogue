from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_year',)


admin.site.register(Book, BookAdmin)
