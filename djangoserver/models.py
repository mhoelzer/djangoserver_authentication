from django.db import models
# db is subsection of django; will be at top b/c you always need models
# obj to act as inheritance
from django.utils import timezone
from django.contrib.auth.models import User


class NewsAuthor(models.Model):
    # name, byline
    name = models.CharField(max_length=50)  # store text
    byline = models.CharField(max_length=250, null=True, blank=True)
    # null=True means can be initialized empty
    # blank=True means it can stay empty
        # null=true means can have nothing instanciated or create w/o data; blank means save w/o data
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name  # won't put a strange-looking string


class NewsItem(models.Model):
    # what do we expect to see on news article
    # body, author, title, date
    body = models.TextField()  # take in up to 65000 char
    title = models.CharField(max_length=50)
    # if .now(), the starttime of server
    date = models.DateTimeField(default=timezone.now)
    # can directly reference diff model
    author = models.ForeignKey(NewsAuthor, on_delete=models.CASCADE)
    # ^^^ any author of news item; if entry linked to in newstable, cascade/delete all articles person wrote

    def __str__(self):
        return self.title 
        # return f"{self.author.name} -- {self.title}"