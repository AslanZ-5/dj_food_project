from django.contrib import admin
from django.urls import path,include
from search.views import search_view
from meals.views import meal_queue_toggle_view
urlpatterns = [
    path('meal-toggle/<int:recipe_id>/',meal_queue_toggle_view,name='meal-toggle'),
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('recipes/',include('recipes.urls')),
    path('accounts/',include('accounts.urls')),
    path('search/', search_view, name='search'),


]
