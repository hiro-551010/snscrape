from django.shortcuts import render
from tweet.forms import PersonForm, KeywordForm
from .application import person, keyword
import pandas as pd
import os

def index(request):
    form = PersonForm()
    context = {
        "form": form 
    }
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            person.main(username)

    return render(request, "tweet/index.html", context)

def search(request):
    form = KeywordForm()
    context = {
        'form': form
    }
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            keywords = request.POST.get("keyword")
            since = request.POST.get("since")
            until = request.POST.get("until")
            keyword.main(keywords, since, until)

    return render(request, "tweet/search.html", context)
