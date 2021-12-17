from django.contrib import admin
from django.urls import path,include
from search.views import search_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('recipes/',include('recipes.urls')),
    path('accounts/',include('accounts.urls')),
    path('search', search_view, name='hx-search')
]
