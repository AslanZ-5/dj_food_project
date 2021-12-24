from django.contrib.auth import get_user_model
from meals.models import Meal
from django.db.models import Sum
from recipes.models import Ingredient
User = get_user_model()
j = User.objects.first()

queue = Meal.objects.by_user(j).pending()
ids = queue.values_list('recipe__ingredient__id', flat=True)
qs = Ingredient.objects.filter(id__in=ids)
data = qs.values("name","unit").annotate(total=Sum('quantity_as_float'))

for d in data:
    print(d)