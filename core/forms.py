from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        print(self.cleaned_data.get('title'))
        if self.cleaned_data.get('title').startswith('T'):
            raise forms.ValidationError('The title can\'t starts with capital "T"')
        return self.cleaned_data
