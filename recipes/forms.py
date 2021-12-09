from django import forms
from .models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    error_css_class = 'rrrr-eerrrror'
    required_css_class = 'ret-cl-tt'
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'recipe name'}),
                           help_text='help me please')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}))

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'direction']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'placeholder': f'Recipe {field}'})

        # self.fields['name'].label = 'Recipe Name'
        # self.fields['name'].widget.attrs.update({'class':'form_control_22',"placeholder":'Recipe Name'})


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']
