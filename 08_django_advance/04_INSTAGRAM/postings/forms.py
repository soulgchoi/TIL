from django import forms
from .models import Posting, Image, Comment


class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('content',)

# 여러개 사진 업로드 가능한 form
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', )
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


