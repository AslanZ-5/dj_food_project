from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save


class Article(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    content = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish = models.DateField(default=timezone.now)

    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    print(args, kwargs)
    instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Article)


def article_post_save(created, instance, *args, **kwargs):
    print('post_save')
    print(args, kwargs)
    if created:
        instance.slug = slugify(instance.title)
    

post_save.connect(article_post_save, sender=Article)
