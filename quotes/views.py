from django.shortcuts import render, redirect, get_object_or_404
from quotes.forms import QuoteForm
from django.contrib.auth.decorators import login_required
from quotes.models import Quote


@login_required
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


@login_required
def show_quote(request, id):
    quote = get_object_or_404(Quote, id=id)
    context = {
        "quote": quote,
    }
    return render(request, "quotes/detail.html", context)
