from django.contrib import admin
from quotes.models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "quote",
        "page",
        "book",
    )
