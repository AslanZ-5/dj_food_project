from django.shortcuts import render
from .models import Meal
from recipes.models import Recipe
from django.http import HttpResponseBadRequest, HttpResponse


def meal_queue_toggle_view(request, recipe_id=None):
    if not request.htmx:
        return HttpResponseBadRequest()
    user = request.user
    user_id = None
    if not user.is_authenticated:
        return HttpResponse('Must be logged in', status=400)
    user_id = user.id
    if user_id is None:
        return
    if request.method == "POST":
        is_valid_recipe = False
        try:
            recipe_obj = Recipe.objects.get(user=user, id=recipe_id)
            is_valid_recipe = True
        except:
            pass
        if is_valid_recipe:
            Meal.objects.toggle_in_queue(user_id, recipe_id)
    is_pending = Meal.objects.by_user_id(user_id).in_queue(recipe_id)
    taggle_label = "Add to meals" if not is_pending else "Remove fom meals"
    context = {'recipe_id': recipe_id,
               'toggle_label': taggle_label,
               'is_pending': is_pending
               }
    return render(request, 'meals/partial/queue-toggle.html', context)
