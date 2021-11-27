from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','added_date','updated_date']
    search_fields = ['title','content']


admin.site.register(Article, ArticleAdmin)
