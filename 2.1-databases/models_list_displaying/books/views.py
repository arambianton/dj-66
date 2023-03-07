import datetime
from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

def books_view(request, publication_date=None):

    template = 'books/books_list.html'
    prev = None
    next = None

    if publication_date:
        # Buscamos el primer libro que tenga la fecha de publicación más alta que la actual
        # Ese libro lo guardamos en la variables next
        next = Book.objects.order_by('pub_date').filter(pub_date__gt=publication_date)
        next = next.first() if next.exists() else None

        # Buscamos el primer libro que tenga la fecha de publicación más baja que la actual
        # Ese libro lo guardamos en la variables prev
        prev = Book.objects.order_by('-pub_date').filter(pub_date__lt=publication_date)
        prev = prev.first() if prev.exists() else None

        # En la variable books buscas todos los libros con fecha de publicación actual
        books = Book.objects.filter(pub_date=publication_date) # book published on publication_date
    else:
        books = Book.objects.all().order_by('pub_date')

    context = {
        'books': books,
        'next': next,
        'prev': prev,
        'publication_date': publication_date,
    }

    return render(request, template, context)

