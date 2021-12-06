from django.contrib import admin
from .models import Recipe, Ingredient


class RecipeIngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'id']
    readonly_fields = ['updated', 'timestamp']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
