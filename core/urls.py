from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.article_search, name='search'),
    path('article/<int:id>/', views.detail, name='detail')
]