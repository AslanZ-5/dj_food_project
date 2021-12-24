from django.shortcuts import render


def meal_queue_toggle_view(request, recipe_id=None):
    context = {'recipe_id': recipe_id}
    return render(request, 'meals/partial/queue-toggle.html', context)
