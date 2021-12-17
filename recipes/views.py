from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm
from .models import Recipe, Ingredient
from django.forms import modelformset_factory
from django.http import HttpResponse, Http404


@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list': qs
    }
    return render(request, 'recipes/list.html', context)


@login_required
def recipe_detail_view(request, id=None):
    hx_url = reverse('hx-detail', kwargs={'id': id})
    context = {
        'hx_url': hx_url,
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_detail_hx_view(request, id=None):
    if not request.htmx:
        raise Http404
    try:
        obj = Recipe.objects.get(id=id, user=request.user)
    except:
        obj = None

    if obj is None:
        return HttpResponse('Not found.')
    context = {
        'obj': obj,
    }
    return render(request, 'recipes/partial/detail.html', context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    print(bool(form.instance.id))
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect":obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)

        return redirect(obj.get_absolute_url())

    return render(request, 'recipes/create-update.html', {'form': form})


@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    new_ingredient_url = reverse('hx-ingredient-create', kwargs={'parent_id':obj.id})
    context = {
        'form': form,
        'object': obj,
        'new_ingredient_url':new_ingredient_url,

    }

    if form.is_valid():
        form.save()
        context['message'] = 'Data is updated'
    if request.htmx:
        return render(request, 'recipes/partial/forms.html', context)
    return render(request, 'recipes/create-update.html', context)


@login_required
def recipe_ingredient_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Recipe.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None

    if parent_obj is None:
        return HttpResponse('Not found.')
    instance = None
    if id is not None:
        try:
            instance = Ingredient.objects.get(recipe=parent_obj, id=id)
        except:
            instance = None
    form = IngredientForm(request.POST or None, instance=instance)
    url = instance.get_hx_edit_url() if instance else reverse('hx-ingredient-create', kwargs={'parent_id':parent_obj.id})

    context = {
        'url':url,
        'object': instance,
        'form': form
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.recipe = parent_obj
        new_obj.save()
        context['object'] = new_obj
        return render(request, 'recipes/partial/ingredient-inline.html', context)
    return render(request, 'recipes/partial/ingredient-form.html', context)
