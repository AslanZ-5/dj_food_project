from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Recipe, Ingredient

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('user6', password='test12345')

    def test_user_pw(self):
        checked = self.user_a.check_password('test12345')
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('user7', password='test12345')
        self.recipe_a = Recipe.objects.create(
            name='gril',
            user=self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='takos',
            user=self.user_a
        )
        self.recipe_ingredient_a = Ingredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound'
        )
        self.recipe_ingredient_b = Ingredient.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='dsdsds',
            unit='pound'
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        qs = self.user_a.recipe_set.all()
        self.assertEqual(qs.count(), 2)

    def test_user_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(),2)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.ingredient_set.all()
        self.assertEqual(qs.count(),2)

    def test_recipe_ingredient_count(self):
        recipe = self.recipe_a
        qs = Ingredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(),2)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = Ingredient.objects.filter(recipe__user = user)
        self.assertEqual(qs.count(),2)

    def test_user_two_level_reverse_relation(self):
        user = self.user_a
        ingredients_ids = list(user.recipe_set.all().values_list('ingredient__id',flat=True))
        qs = Ingredient.objects.filter(id__in=ingredients_ids)
        self.assertEqual(qs.count(),2)

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient_b.quantity_as_float)
