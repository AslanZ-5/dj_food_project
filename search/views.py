from django.shortcuts import render


def search_view(request):
    query = request.GET.get('q')
    context = {
        'query': query
    }
    template = "search/results.html"
    if request.htmx:
        template = "search/partial/results.html"
    return render(request, template, context)