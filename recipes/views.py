from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm
from .models import Recipe, Ingredient
from django.forms import modelformset_factory
from django.http import HttpResponse

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list': qs
    }
    return render(request, 'recipes/list.html', context)


@login_required
def recipe_detail_view(request, id=None):
    hx_url = reverse('hx-detail',kwargs={'id':id})
    context = {
        'hx_url': hx_url,
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_detail_hx_view(request, id=None):
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None

    if obj is None:
        return HttpResponse('Not found.')
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        'obj': obj,
    }
    return render(request, 'recipes/partial/detail.html', context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())

    return render(request, 'recipes/create.html', {'form': form})


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    ingredient_form_set = modelformset_factory(Ingredient, form=IngredientForm, extra=0)
    qs = obj.ingredient_set.all()
    form_set = ingredient_form_set(request.POST or None, queryset=qs)
    context = {
        'form': form,
        'form_2': form_set
    }
    print(form.is_valid(), form_set.is_valid())
    if form.is_valid() and form_set.is_valid():
        parent = form.save(commit=False)
        parent.save()
        for ing in form_set:
            child = ing.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'Data is updated'
    if request.htmx:
        return render(request, 'recipes/partial/forms.html', context)
    return render(request, 'recipes/update.html', context)
