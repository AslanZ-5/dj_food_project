# Generated by Django 3.2.9 on 2021-11-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]
