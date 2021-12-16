from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.recipe_list_view, name='list'),
    path('detail/<int:id>/',views.recipe_detail_view, name='detail'),
    path('hx/<int:id>/',views.recipe_detail_hx_view, name='hx-detail'),
    path('create/', views.recipe_create_view, name='create'),
    path('update/<int:id>/', views.recipe_update_view, name='update'),
    path('hx/<int:parent_id>/ingredient/<int:id>',views.recipe_ingredient_update_hx_view, name='hx-ingredient-update')

]