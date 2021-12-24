from django.contrib.auth import get_user_model
from meals.models import Meal
from django.db.models import Sum
from recipes.models import Ingredient

User = get_user_model()


def generate_meal_queue_totals(user):
    queue = Meal.objects.get_queue(user, include_ingredients=True)
    ids = queue.values_list('recipe__ingredient__id', flat=True)
    qs = Ingredient.objects.filter(id__in=ids)
    return qs.values("name", "unit").annotate(total=Sum('quantity_as_float'))
