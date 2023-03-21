from django.urls import path
from quotes.views import add_quote, show_quote


urlpatterns = [
    path("add/", add_quote, name="add_quote"),
    path("<int:id>/", show_quote, name="show_quote"),
]
