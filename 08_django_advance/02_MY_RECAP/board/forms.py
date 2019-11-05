from django import forms
from .models import Article


class ArticleModelForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=50)

    class Meta:
        model = Article
        fields = '__all__'