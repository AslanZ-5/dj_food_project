from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from .models import Recipe


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
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data is updated'
    return render(request,'recipes/create.html',context)
