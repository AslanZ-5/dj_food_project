from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        print(self.cleaned_data.get('title'))
        if self.cleaned_data.get('title').startswith('T'):
            self.add_error('title', 'This title can\'t starts with capital "T"')
            # raise forms.ValidationError('The title can\'t starts with capital "T"')
        if self.cleaned_data.get('content').startswith('A'):
            self.add_error('title', 'This content can\'t starts with capital "A"')
        return self.cleaned_data
