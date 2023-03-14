from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField(max_length=800)
    summary = models.TextField()
    started = models.DateField(null=True, blank=True)
    finished = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
