from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish = models.DateField(default=timezone.now)
