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
    return HttpResponse(render_to_string('core/home.html', {'title': Article.objects.get(id=1).title,
                                                            'content': Article.objects.get(id=1).content}))


def detail(request,id):
    obj = Article.objects.get(id=id)
    return render(request,'detail.html', {'object':obj})