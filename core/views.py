from django.shortcuts import render
from django.shortcuts import redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
import random
from django.http import Http404

a = random.randint(10, 10000)



def home(request):
    context = {'objects': Article.objects.all()}
    return render(request, 'core/home.html', context=context)


# def article_search(request):
#     try:
#         query = request.GET.get('q')
#     except:
#         query = None
#     qs = Article.objects.all()
#     if query is not None:
#         qs = Article.objects.search(query)
#     context = {'objects': qs }
#
#     return render(request, 'search.html', context=context)


def detail(request, slug):
    try:
        obj = Article.objects.get(slug=slug)
    except:
        raise Http404
    return render(request, 'detail.html', {'object': obj})


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            # Article.objects.create(title=request.POST.get('title'), content=request.POST.get('content'))
            obj = form.save()
            context['form'] = ArticleForm()
            return redirect(obj.get_absolute_url())

    return render(request, 'create.html', context=context)
