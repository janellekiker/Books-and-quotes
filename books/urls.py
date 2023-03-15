from django.urls import path
from books.views import home, book_list


urlpatterns = [
    path("", home, name="home"),
    path("list/", book_list, name="book_list"),
]
