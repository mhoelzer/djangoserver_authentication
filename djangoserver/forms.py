from django import forms
from djangoserver.models import NewsAuthor


class NewsAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=NewsAuthor.objects.all())
    # author = forms.ChoiceField()
    date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    # date = forms.DateTimeField(
    #     widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"}))

    # asdf = [(a.id, a.user.username) for a in NewsAuthor.objects.all()]
    # choices = [(1, "Bob"), (2, "Kyle"), (3, "Travis")]
    # author = forms.ChoiceField(choices=choices)


class SignupForm(forms.Form):
    name = forms.CharField(max_length=500)
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
