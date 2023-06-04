from django.shortcuts import render, redirect
from books.models import Book
from django.core.paginator import Paginator
from django.db.models import Q


def index_view(request):
    return redirect('books')


def books_view(request):
    search_term = request.GET.get('search', '')
    
    if search_term:
        books = Book.objects.filter(
            Q(name__icontains=search_term) |
            Q(author__icontains=search_term) |
            Q(pub_year__contains=search_term) | 
            Q(publisher__icontains=search_term)
        )
    else:
        books = Book.objects.all()

    template = 'books/books_list.html'
    context = {
        'books': books,
        'show_search': True,
    }
    return render(request, template, context)


def pub_year_view(request, pub_year):
    books = Book.objects.filter(pub_year=pub_year)

    prev_date = Book.objects.filter(pub_year__lt=pub_year).order_by('-pub_year').first()
    next_date = Book.objects.filter(pub_year__gt=pub_year).order_by('pub_year').first()

    template = 'books/books_list.html'
    context = {
        'books': books,
        'prev_date': prev_date.pub_year if prev_date else None,
        'next_date': next_date.pub_year if next_date else None,
        'show_search': False,
    }
    return render(request, template, context)
