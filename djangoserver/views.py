from django.shortcuts import render, reverse, HttpResponseRedirect
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from djangoserver.models import NewsItem, NewsAuthor
from djangoserver.forms import NewsAddForm, SignupForm, LoginForm

# doenst have to be called index


def index(request):
    html = "index.html"
    items = NewsItem.objects.all()
    return render(request, html, {"stuff": items})


@login_required()
def newsadd(request):
    html = "newsadd.html"
    form = None
    if request.method == "POST":
        # form = NewsAddForm(request.user, request.POST)
        # assumes form can take in req.usr
        form = NewsAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            NewsItem.objects.create(
                title=data["title"],
                body=data["body"],
                author=data["author"],
                # author=NewsAuthor.objects.filter(id=data["author"]).first(),
                date=data["date"]
            )
            return render(request, "thanks.html")
    else:
        form = NewsAddForm()
    return render(request, html, {"form": form})


def signup_view(request):
    html = "generic_form.html"
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["email"], data["password"])
            login(request, user)
            NewsAuthor.objects.create(name=data["name"], user=user)
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = "generic_form.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
                # /&next= 
    else:
        form = LoginForm()
    return render(request, html, {"form": form})
