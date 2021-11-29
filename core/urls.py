from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.article_search, name='search'),
    path('article/<slug:slug>/', views.detail, name='detail'),
    path('article/create', views.article_create_view, name='create'),
]