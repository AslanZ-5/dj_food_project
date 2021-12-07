from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, IngredientForm
from .models import Recipe,Ingredient
from django.forms import modelformset_factory

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        'object_list': qs
    }
    return render(request, 'recipes/list.html', context)


@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        'obj': obj,
    }
    return render(request, 'recipes/detail.html', context)


@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())

    return render(request,'recipes/create.html',{'form':form})



@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id,user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    ingredient_form_set = modelformset_factory(Ingredient,form=IngredientForm,extra=0)
    qs = obj.ingredient_set.all()
    form_set = ingredient_form_set(request.POST or None,queryset=qs)
    context = {
        'form': form,
        'form_2': form_set
    }

    if form.is_valid() and form_set.is_valid():
        parent = form.save(commit=False)
        parent.save()
        for ing in form_set:
            child = ing.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'Data is updated'
    return render(request,'recipes/create.html',context)
