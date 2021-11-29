from django.test import TestCase
from .models import Article
from django.utils.text import slugify
from .utile import slugify_instance_title

class ArticleTestCase(TestCase):

    def setUp(self):
        self.number_of_articles = 50
        for i in range(self.number_of_articles):

            Article.objects.create(title='hello world', content=f'ads{i}')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_articles)

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

    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        slugify_instance_title(obj,save=False)
        self.assertEqual(obj.slug,f'{slugify(obj.title)}-{obj.id}')

    def test_of_uniqueness_all_slugs(self):
        slug_list = Article.objects.all().values_list('slug',flat=True)
        unique_slug_list = set(slug_list)
        self.assertEqual(len(unique_slug_list),len(slug_list))
