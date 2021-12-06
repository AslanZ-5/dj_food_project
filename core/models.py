from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
import random
from django.db.models import Q
from .utile import slugify_instance_title
from django.urls import reverse


class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == '':
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish = models.DateField(default=timezone.now)
    objects = ArticleManager()

    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug': self.slug})
    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(created, instance, *args, **kwargs):
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(article_post_save, sender=Article)
