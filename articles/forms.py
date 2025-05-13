from django import forms
from .models import Articles


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'text')
