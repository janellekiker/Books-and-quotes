from django.forms import ModelForm
from books.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "picture",
            "summary",
            "started",
            "finished",
        ]

class BookUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
