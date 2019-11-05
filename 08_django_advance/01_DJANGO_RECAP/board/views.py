from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article, Comment
from .forms import ArticleModelForm, CommentModelForm
from IPython import embed
# CRUD

"""
# form 예시 (modelform 이랑 다름)
from .forms import ArticleForm
def new_article_with_form(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            article = Article()
            # article.title = request.POST.get('title')  # 검증되지 않은 데이터, 쓰지 마!
            article.title = form.cleaned_data.get('title')  # 검증된 데이터
            article.content = form.cleaned_data.get('content')
            article.save()
            # form 은 article 이라는 model 과 아무 상관 없기 때문에
            # 데이터가 자동으로 들어가지 않아서
            # article 에 관해 다 써줘야 함
            return redirect(article)
    else:
        form = ArticleForm()
    return render(request, 'board/new.html', {
        'form': form,
    })
"""


# 저장은 create, url 은 new 로 하는 것이 보통
@require_http_methods(['GET', 'POST'])
# ㄴ 어차피 get 이랑 post 밖에 없는데 왜? > 사실 더 있음..
# 그래서 이렇게 두 개 다 써야 완성도가 높아짐
def new_article(request):
    What = 'new'
    # 요청 GET/POST 확인
    # 만약 POST 라면
    if request.method == 'POST':
        # ArticleModelForm 의 인스턴스를 생성하고 Data 를 채운다. (binding)
        form = ArticleModelForm(request.POST)
        # shell 을 열어서 시간을 멈춘다..!
        # embed()
        # shell 에서
        # form
        # form.is_valid()
        # form.cleaned_data  > 통과한 데이터
        # form.cleaned_data.get('content')
        # form.as_p()

        # binding 된 form 이 유효한지 체크한다.
        if form.is_valid():
        # 유효하다면, (form을) 저장한다.
            # 여기서 확인하면서 save 하면 아래에서 또 db에 저장되나?
            # embed()
            # save 한 번 하면서 소비돼서 또 저장되지는 않음 (혹은 수정에 가깝게 동작하거나)
            article = form.save()
            # 저장한 article:article_detail 로 redirect
            return redirect(article)  # model 에 get_absolute_url 했기때문에 가능
        # 유효하지 않다면,
        # else:
            # 유효하지 않은 입력데이터를 담은 html 과 에러메시지를 사용자에게 보여준다.
            # return render(request, 'board/new.html', {
            #     'form': form,
                # 유효성 검사 탈락했을 때 데이터랑 에러메시지 받은걸로 변함!
                # 그대로 가져가면 됨
            # })
    # GET 이라면
    else:
        # 비어있는 form(HTML 생성기) 을 만든다.
        form = ArticleModelForm()
        # form 과 html 을 사용자에게 보여준다.
    # 또는 return 하기 직전에 embed 넣고 확인
    # embed()
    return render(request, 'board/form.html', {
        'form': form,
        'What': What,
    })


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # foreignkey 설정하는 순간 article 을 쉽게 불러올 수 있음
    # comments 불러오는 함수 따로 없고 article 에서 다 볼 수 있게
    comments = article.comment_set.all().order_by('-id')  # order ~~ 최근순 정렬
    # == Comment.objects.filter(article_id=article.id)
    comment_form = CommentModelForm()
    return render(request, 'board/detail.html', {
        'article': article,
        #
        'comments': comments,
        'comment_form': comment_form,
    })


@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    What = 'edit'
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = ArticleModelForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
        # else:
        #     return render(request, 'board/edit.html', {
        #         'form': form,
        #     })
    else:
        # article = get_object_or_404(Article, id=id)
        # data 가 들어가 있는 form
        # 이 때 data 는 앞에서 받은 article
        form = ArticleModelForm(instance=article)
        # return render(request, 'board/edit.html', {
        # 'form': form,
        # })
    return render(request, 'board/form.html', {
        'form': form,
        'What': What,
    })


@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Aritcle, id=article_id)
    article.delete()
    return redirect('board:article_list')


@require_POST
def new_comment(request, article_id):
    # 1:N 으로 종속된 데이터이기 때문에 연결고리가 필요함
    # /board/comment/new/id/
    # /board/comment/asdf/id/
    # detail page > /board/articles/article_id/comments/comment_id/new,delete, .. > 이게 맞는듯!
    article = get_object_or_404(Article, id=article_id)
    # comment = Comment()
    # comment.content = request.POST.get('comment_content')
    # comment.article_id = article.id
    # 왜 아래처럼 바로 쓰지 않을까?
    # get_object~~ 로 불러오면서 검증과정을 거침
    # comment.article_id = article_id
    # comment.save()

    # comment 도 form 으로 써보기
    # 데이터 받아서 저장해야함
    form = CommentModelForm(request.POST)
    # form.errors
    # embed()
    if form.is_valid():
        # comment = form.save() 라고 안쓰는 이유는,
        # article 은 detail 페이지로 redirect 해야하는데, comment 는 detail 페이지 필요 없음
        # 굳이 변수 하나를 늘릴 필요가 없어짐
        # form.save()
        # save 할 때 NOT NULL constratint failed > board_comment.article_id 가 없기 때문
        comment = form.save(commit=False)
        # save 때 에러 안나기 위해,
        # save 하는 척; 뭐가 저장되긴 함
        # comment = Comment()
        # comment.content = request.POST.get('content')
        # 와 같은 상태라고 할 수 있음
        # 일단 세이브 하는 척 하고 > id 넣어주고 > 진짜 세이브
        comment.article_id = article.id
        comment.save()
        return redirect(article)


@require_POST
def delete_comment(request, article_id, comment_id):
    # article 을 먼저 찾음
    # article = get_object_or_404(Article, id=article_id)
    # article 에서 넘어온 comment_id 를 찾음
    # SELECT * FROM articles WHERE id=article_id
    # comment = get_object_or_404(Comment, id=comment_id)
    # comment 가 article 의 모든 comment 정보 가져온 안에 있다면,
    # SELECT * FROM comments WHERE id=comment_id

    comment = get_object_or_404(Comment, id=comment_id, article_id=article_id)
    # 안전함 + 시간복잡도 다 챙길 수 있는 방법

    # if comment in article.comment_set.all():
        # comment 를 지우고
    comment.delete()
    # 해당 article 페이지로 다시 이동
    return redirect(article)
    """
    comment = get_objects_or_404(Comment, id=comment_id)
    comment.delete()
    > db 에서 삭제
    return redirect(comment.article)
    > 메모리에 아직 남아 있음
    db 에서 삭제되는 시점과 메모리에서 휘발되는 시점이 다름 
    """