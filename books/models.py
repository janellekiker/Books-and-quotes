from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(max_length=800)
    summary = models.TextField()
    started = models.DateField(null=True, blank=True)
    finished = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="quotes",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
