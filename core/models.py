from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
import random

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


def slugify_instance_title(instance,new_slug=None, save=False):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    qs = Article.objects.filter(slug = slug).exclude(id=instance.id)
    if qs.exists():
        num = random.randint(1,1000)
        slug = f'{slug}-{num}'
        return slugify_instance_title(instance,save=save,new_slug=slug)
    instance.slug = slug
    if save:
        instance.save()
def article_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')

    if instance.slug is None:
        slugify_instance_title(instance)



pre_save.connect(article_pre_save, sender=Article)


def article_post_save(created, instance, *args, **kwargs):
    print('post_save')

    if created:
        slugify_instance_title(instance,save=True)


post_save.connect(article_post_save, sender=Article)
