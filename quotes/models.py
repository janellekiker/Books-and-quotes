from django.db import models
from books.models import Book


class Quote(models.Model):
    quote = models.TextField()
    page = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)
    book = models.ForeignKey(
        Book,
        related_name="book",
        on_delete=models.CASCADE,
    )
