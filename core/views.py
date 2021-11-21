from django.shortcuts import render
from django.http import HttpResponse
import random
a = random.randint(10,10000)
h = f'''
    <h1> Helloewe - {a} <h1>
'''


def home(request):
    return HttpResponse(h)
