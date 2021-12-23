from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from recipes.models import Recipe,Ingredient
from .models import Meal,MealStatus
User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('user6', password='test12345')

    def test_user_pw(self):
        checked = self.user_a.check_password('test12345')
        self.assertTrue(checked)


class MealTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('user7', password='test12345')
        self.user_id = self.user_a.id
        self.recipe_a = Recipe.objects.create(
            name='gril',
            user=self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='takos',
            user=self.user_a
        )
        self.recipe_c = Recipe.objects.create(
            name='takosddddd',
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

        self.meal = Meal.objects.create(
            user=self.user_a,
            recipe = self.recipe_a
        )
        meal_b = Meal.objects.create(
            user=self.user_a,
            recipe=self.recipe_a,
            status= MealStatus.COMPLETED
        )

    def test_pending_meals(self):
        qs = Meal.objects.all().pending()
        self.assertEqual(qs.count(),1)
        qs2 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs.count(), 1)

    def test_completed_meals(self):
        qs = Meal.objects.all().completed()
        self.assertEqual(qs.count(), 1)
        qs2 = Meal.objects.by_user_id(self.user_id).completed()
        self.assertEqual(qs.count(), 1)

    def test_add_item_via_toggle(self):
        meal_b = Meal.objects.create(
            user=self.user_a,
            recipe=self.recipe_a,
           )
        qs1 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs1.count(),2)
        added = Meal.objects.toggle_in_queue(self.user_id,self.recipe_c.id)
        qs2 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs2.count(),3)
        self.assertTrue(added)

    def test_remove_item_via_toggle(self):
        added = Meal.objects.toggle_in_queue(self.user_id, self.recipe_a.id)
        qs2 = Meal.objects.by_user_id(self.user_id).pending()
        self.assertEqual(qs2.count(), 0)
        self.assertFalse(added)
