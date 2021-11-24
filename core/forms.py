from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()

    class Meta:
        model = Article
        fields = ['title', 'content']
    def clean(self):
        data = self.cleaned_data.get('title')
        qs = Article.objects.filter(title__icontains = data)
        if qs.exists():
            self.add_error('title','this title already taken')

# class ArticleForms(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()
#
#     def clean(self):
#         print(self.cleaned_data.get('title'))
#         if str(self.cleaned_data.get('title')).startswith('T'):
#             self.add_error('title', 'This title can\'t starts with capital "T"')
#             # raise forms.ValidationError('The title can\'t starts with capital "T"')
#         if self.cleaned_data.get('content').startswith('A'):
#             self.add_error('content', 'This content can\'t starts with capital "A"')
#         return self.cleaned_data
