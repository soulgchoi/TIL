from django import forms
from .models import Posting, Comment

class PostingModelForm(forms.ModelForm):  # data 의 입력과 검증 & html ( html 부분은 굳이 안써도 됨 )
    # modelform 이 meta 라는 클래스 안에서 찾도록
    # column 값을.. 읽는.. 그런 것 때문...
    class Meta:
        model = Posting
        fields = ('content', 'image', 'icon')



class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)

    class Meta:
        model = Comment
        fields = ('content',)  # , 찍어서 iterable 이 되어야 함