from django.db import models
from books.models import Book


class Quote(models.Model):
    quote = models.TextField()
    note = models.TextField(null=True, blank=True)
    page = models.CharField(max_length=100)
    book = models.ForeignKey(
        Book,
        related_name="quotes",
        on_delete=models.CASCADE,
    )
