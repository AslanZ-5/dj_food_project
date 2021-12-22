from django.contrib import admin
from .models import Recipe, Ingredient,IngredientImage

admin.site.register(IngredientImage)
class RecipeIngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 0
    readonly_fields = ['quantity_as_float']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'id']
    readonly_fields = ['updated', 'timestamp']
    raw_id_fields = ['user']


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name','id']
    readonly_fields = ['quantity_as_float','as_mks','as_imperial']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient,IngredientAdmin)
