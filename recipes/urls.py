from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.recipe_list_view, name='list'),
    path('detail/<int:id>/',views.recipe_detail_view, name='detail'),
    path('delete/<int:id>/', views.recipe_delete_view, name='delete'),
    path('hx/<int:id>/',views.recipe_detail_hx_view, name='hx-detail'),
    path('create/', views.recipe_create_view, name='create'),
    path('upload/<int:parent_id>/', views.ingredient_image_upload_view, name='upload-img'),
    path('update/<int:id>/', views.recipe_update_view, name='update'),
    path('hx/<int:parent_id>/ingredient/<int:id>/',views.recipe_ingredient_update_hx_view, name='hx-ingredient-update'),
    path('<int:parent_id>/ingredient/<int:id>/delete/',views.ingredient_delete_view, name='ingredient-delete'),
    path('hx/<int:parent_id>/ingredient/',views.recipe_ingredient_update_hx_view, name='hx-ingredient-create')

]