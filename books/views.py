from django.shortcuts import render
from books.models import Book


def book_list(request):
    books = Book.objects.all()
    context = {
        "book_list": books,
    }
    return render(request, "books/list.html", context)
