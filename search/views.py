from django.shortcuts import render
from core.models import Article
from recipes.models import Recipe

SEARCH_TYPE_MAPPING = {
    'articles': Article,
    'article': Article,
    'recipe': Recipe,
    'recipes': Recipe
}

def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    Klass = Recipe
    if search_type in SEARCH_TYPE_MAPPING.keys():
        Klass = SEARCH_TYPE_MAPPING[search_type]
    qs = Klass.objects.search(query=query)
    context = {
        "query": query,
        'queryset': qs,
    }
    template = "search/results_view.html"
    if request.htmx:

        template = "search/partial/results.html"
    return render(request, template, context)