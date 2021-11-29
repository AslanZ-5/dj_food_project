from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
import random
from django.http import Http404
a = random.randint(10, 10000)


# h = f'''
#     <h1> Helloewe - {a}<h1>
# '''


def home(request):
    context = {'objects': Article.objects.all()}
    return render(request, 'core/home.html', context=context)


def article_search(request):
    try:
        query = int(request.GET.get('query'))
    except:
        query = None
    context = {'object': Article.objects.get(id=query)}
    return render(request, 'home.html', context=context)


def detail(request, slug):
    try:
        obj = Article.objects.get(slug=slug)
    except:
        raise Http404
    return render(request, 'detail.html', {'object': obj})


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            # Article.objects.create(title=request.POST.get('title'), content=request.POST.get('content'))
            form.save()
            context['form'] = ArticleForm()

    return render(request, 'create.html', context=context)
