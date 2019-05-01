from django import forms
from djangoserver.models import NewsAuthor


class NewsAddForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=NewsAuthor.objects.all())
    date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
    # date = forms.DateTimeField(
    #     widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"}))

    # asdf = [(a.id, a.user.username) for a in NewsAuthor.objects.all()]
    # choices = [(1, "Bob"), (2, "Kyle"), (3, "Travis")]
    # author = forms.ChoiceField(choices=choices)
