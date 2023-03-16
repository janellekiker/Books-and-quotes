from django.shortcuts import render, redirect
from quotes.forms import QuoteForm


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = QuoteForm()
    context = {
        "form": form,
    }
    return render(request, "quotes/add.html", context)
