# Generated by Django 3.2.9 on 2021-12-22 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_ingredientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientimage',
            name='image',
            field=models.ImageField(upload_to='recipes/'),
        ),
    ]
