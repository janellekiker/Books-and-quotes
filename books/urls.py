from django.urls import path
from books.views import home, book_list, add_book, edit_book, show_book


urlpatterns = [
    path("", home, name="home"),
    path("list/", book_list, name="book_list"),
    path("add", add_book, name="add_book"),
    path("<int:id>/edit/", edit_book, name="edit_book"),
    path("<int:id>/quotes/", show_book, name="show_book"),
]
