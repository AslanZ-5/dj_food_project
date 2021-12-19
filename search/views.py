from django.shortcuts import render


def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')

    context = {
        "query": query
    }
    template = "search/results_view.html"
    if request.htmx:

        template = "search/partial/results.html"
    return render(request, template, context)