from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','added_date','publish','slug']
    search_fields = ['title','content']
    raw_id_fields = ['user']


admin.site.register(Article, ArticleAdmin)
