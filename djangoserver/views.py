from django.shortcuts import render
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from djangoserver.models import NewsItem

# doenst have to be called index


def index(request):
    html = "index.html"
    items = NewsItem.objects.all()
    return render(request, html, {"stuff": items})
