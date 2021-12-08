from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    error_css_class = 'rrrr-eerrrror'
    required_css_class = 'ret-cl-tt'
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'recipe name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'description'}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'direction']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']
