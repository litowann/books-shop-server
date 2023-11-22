from django.shortcuts import render
from .models import Book


def books_list(request):
    book = Book.objects.all()
    context = {
        'books_list': book
    }

    return render(request, "book/books_list.html", context)