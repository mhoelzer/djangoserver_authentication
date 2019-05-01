from django.shortcuts import render
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from djangoserver.models import NewsItem, NewsAuthor
from djangoserver.forms import NewsAddForm

# doenst have to be called index


def index(request):
    html = "index.html"
    items = NewsItem.objects.all()
    return render(request, html, {"stuff": items})


def newsadd(request):
    html = "newsadd.html"
    form = None
    if request.method == "POST":
        form = NewsAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            NewsItem.objects.create(
                title=data["title"],
                body=data["body"],
                author=data["author"],
                date=data["date"]
            )
            return render(request, "thanks.html")
    else:
        form = NewsAddForm()
    return render(request, html, {"form": form})
