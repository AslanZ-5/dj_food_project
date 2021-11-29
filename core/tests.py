from django.test import TestCase
from .models import Article
from django.utils.text import slugify


class ArticleTestCase(TestCase):

    def setUp(self):
        for i in range(5):
            Article.objects.create(title='hello world', content=f'ads{i}')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), 5)

    def test_slug_first(self):
        obj = Article.objects.all().first()
        slug = obj.slug
        title = obj.title
        self.assertEqual(slug, slugify(title))

    def test_slug_more_than_one(self):
        qs = Article.objects.exclude(slug__iexact='hello-world')
        for i in qs:
            title = slugify(i.title)
            slug = i.slug
            self.assertEqual(slug,f'{title}-{i.id}')
