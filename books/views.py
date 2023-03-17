from django.shortcuts import render, redirect, get_object_or_404
from books.models import Book
from books.forms import BookForm, BookUpdateForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "books/home.html")


@login_required
def book_list(request):
    books = Book.objects.filter(owner=request.user)
    context = {
        "book_list": books,
    }
    return render(request, "books/list.html", context)


@login_required
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(False)
            book.owner = request.user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()

    context = {
        "form": form,
    }

    return render(request, "books/add.html", context)


@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    context = {
        "book_object": book,
        "form": form,
    }

    return render(request, "books/edit.html", context)


@login_required
def show_book(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        "book": book
    }
    return render(request, "books/detail.html", context)
