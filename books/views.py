from django.shortcuts import render, redirect
from books.models import Book
from books.forms import BookForm


def home(request):
    return render(request, "books/home.html")

def book_list(request):
    books = Book.objects.all()
    context = {
        "book_list": books,
    }
    return render(request, "books/list.html", context)

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()

    context = {
        "form": form,
    }

    return render(request, "books/add.html", context)
