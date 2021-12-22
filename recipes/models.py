from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from .validator import validator_unit_of_measure
from .utils import number_str_to_float
import pint
from django.db.models import Q
from django.shortcuts import reverse
import pathlib
import uuid


class RecipeQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()  # return empty queryset
        lookups = (Q(name__icontains=query) |
                   Q(description__icontains=query) |
                   Q(direction__icontains=query))
        return self.filter(lookups)


class RecipeManager(models.Manager):
    def get_queryset(self):
        return RecipeQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    objects = RecipeManager()

    @property
    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.pk})

    def get_hx_url(self):
        return reverse('hx-detail', kwargs={'id': self.pk})

    def get_edit_url(self):
        return reverse('update', kwargs={"id": self.pk})

    def get_delete_url(self):
        return reverse('delete', kwargs={"id": self.pk})

    def get_ingredient_children(self):
        return self.ingredient_set.all()


# making filename unique
def recipe_ingredient_image_upload_handler(instance, filename):
    """
    This function must accept two arguments and return a Unix-style path (with forward slashes)
    to be passed along to the storage system. The two arguments are:

        - instance   An instance of the model where the Filefield is defined
        - filename  The filename that was originally given to the file. This may or may not
            be taken into account when determining the final destination path
     """
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f'recipes/{new_fname}{fpath.suffix}'


class IngredientImage(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=recipe_ingredient_image_upload_handler)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validator_unit_of_measure])
    description = models.TextField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def convert_to_system(self, system='mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement

    def as_mks(self):
        measurement = self.convert_to_system(system='mks')
        return measurement.to_base_units()

    def as_imperial(self):
        measurement = self.convert_to_system(system='imperial')
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)

    def get_hx_edit_url(self):
        return reverse('hx-ingredient-update', kwargs={'id': self.pk, 'parent_id': self.recipe.id})

    def get_delete_url(self):
        return reverse('ingredient-delete', kwargs={'parent_id': self.recipe.id, "id": self.pk})
