from django.contrib import admin
from django.urls import path

from books.views import books_view, index_view, pub_year_view


urlpatterns = [
    path('', index_view, name='index'),
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books'),
    path('books/<int:pub_year>/', pub_year_view, name='pub_year'),
]
