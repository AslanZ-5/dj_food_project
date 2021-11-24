from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title=title)
        print(qs)
        if qs.exists():
            self.add_error('title', 'this title already taken')
        return data

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
