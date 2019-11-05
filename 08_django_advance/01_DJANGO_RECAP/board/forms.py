from django import forms
from .models import Article, Comment
# Forms.Form => Data 입력 및 검증 + HTML 생성
#            => Model 정보를 모름
# Forms.ModelForm => Data 입력/검증 + HTML 생성, 한겹 더 감싸서 이것저것 기능 추가하기, 그냥 부가적인 것
#                 => Model 정보를 알고있음


# article 이라는 model 에 대한 form
class ArticleModelForm(forms.ModelForm):
    # 1. Data 입력 및 검증
    # 2. HTML 생성
    title = forms.CharField(min_length=2, max_length=100)
    # title = forms.EmailField(min_length=3, required=False)
    # ㄴ 얘는 유효성 검사, valid data, 데이터에 들어갈 수 있는지
    # content = forms.Textarea

    class Meta:
        model = Article
        fields = '__all__'
    # model form 은 model 이 뭔지 지정해주는 것이 매우 중요

"""
# 그냥 form 으로 만드는 예시
class ArticleForm(forms.From):
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField()
    # content 무조건 있어야 함
    # 모든 column 써줘야 함
# 상대적으로 기능이 더 적다
# views 추가로 볼 것
"""


# model 은 그냥 column 만드는 정도,
# form 에서는 데이터의 유효성을 검사하고 HTML form 태그를 핸들링할 수 있음
# meta class > python 에서 개념과 다름
# django 에서 meta 는 일종의 예약어..


class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200)
    # 200 넘어가면 에러, 저장 안됨 (200을 검증)

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('content',)
        # id 는 내 담당 아니야! content 만 볼거임
        # id 검증 X, content 검증



