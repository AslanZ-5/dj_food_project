from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.recipe_list_view, name='list'),
    path('detail/<int:id>/',views.recipe_detail_view, name='detail'),
    path('create/', views.recipe_create_view, name='create'),
    path('update/<int:id>/', views.recipe_update_view, name='update'),

]