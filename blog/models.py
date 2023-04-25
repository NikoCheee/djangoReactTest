from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.CharField(max_length=120)
