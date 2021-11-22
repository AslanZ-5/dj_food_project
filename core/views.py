from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template.loader import render_to_string
import random

a = random.randint(10, 10000)


# h = f'''
#     <h1> Helloewe - {a}<h1>
# '''


def home(request):
    context = {'objects': Article.objects.all()}
    return HttpResponse(render_to_string('core/home.html', context=context))


def article_search(request):
    try:
        query = int(request.GET.get('query'))
    except:
        query = None
    print(query)
    context = {'object':Article.objects.get(id=query)}
    return render(request, 'home.html', context=context)


def detail(request, id):
    obj = Article.objects.get(id=id)
    return render(request, 'detail.html', {'object': obj})
