from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Posting, Comment
# forms 작성해서 create 새로 만들 것임
from .forms import PostingModelForm, CommentModelForm
# 인증된 user 만 접속할 수 있도록 만들기
from django.contrib.auth.decorators import login_required

# decorator 추가
# @login_required#(login_url='/users/login/') 꼭 할 필요는...  # login 이 안되어있으면 무조건 /accounts/login/ 으로 redirect
               # settings 에서 상수로 LOGIN_URL 만들 수도 있다
# login 요청에 대해서
@require_GET
# GET 응답을 받아
# 아래 함수 실행
def posting_list(request):
    # nickname = request.COOKIES.get('nickname')  # cookie 꺼내는 것 보기
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
        # 'nickname': nickname,
    })


@login_required
@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()   # related name 때문 ( 없으면 posting.comment_set.all() )
    if posting.like_users.filter(id=request.user.id).exists():
        is_like = True 
    else:
        is_like = False
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
        'is_like': is_like,
    })


# @require_POST
# def create_posting(request):
#     posting = Posting()
#     posting.content = request.POST.get('content')
#     posting.icon = ''
#     # 이 파일은 내가 지정한 폴더(/media/)에 저장되고, db 에 저장되는 것은 아니다
#     posting.image = request.FILES.get('image')
#     posting.save()
#     return redirect(posting)  # get_absolute_url 있으니까 / 없으면 ('sns:posting_detail', posting.id)


@login_required
@require_POST
def create_posting(request):
    # form = PostingModelForm()  # () == 아무 내용 없는 modelform 생성 / (request.POST) == post 요청 내용을 검증&저장 준비
    form = PostingModelForm(request.POST, request.FILES)  # image 를 FILES 로 받았기 때문에 따로 받아야 함
    if form.is_valid():  # 검증
        posting = form.save(commit=False)  # 저장 > Posting 객체를 return
        # posting.user_id = request.user.id
        posting.user = request.user  # user 객체로 맵핑 가능
        # anonymous 라면? > login_required 때문에 불가능
        posting.save()
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page


@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.user == posting.user:
        posting.delete()
    return redirect('sns:posting_list')


@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인
    if form.is_valid():  # content 만 값을 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 척 하고, Comment 객체 return
        # comment.posting_id = posting.id
        # comment 에 posting_id 가 있나 없나 어디서 확인? > db 에 있으니까
        comment.posting = posting
        # save 하면 posting_id 쓰는것과 똑같음, 숫자를 넣느냐 객체를 넣느냐
        comment.user = request.user
        comment.save()
    return redirect(posting)


@login_required
@require_POST
def delete_comment(request, posting_id, comment_id):
    comment = get_object_or_404(Comment, posting_id=posting_id, id=comment_id)
    comment.delete()
    return redirect(comment.posting)


@login_required
@require_POST
def toggle_like(request, posting_id):
    user = request.user
    posting = get_object_or_404(Posting, id=posting_id)
    # if user in posting.like_users.all():
    if posting.like_users.filter(id=user.id).exists():  # 데이터 전부 받아오면 너무 많으니까...
        posting.like_users.remove(user)
    else:
        posting.like_users.add(user)  # create
        # == user.like_posting.add(posting)
    return redirect(posting)


# @login_required
# @require_POST
# def dislike(request, posting_id):
#     user = request.user
#     posting = get_object_or_404(Posting, id=posting_id)
#     posting.like_users.remove(user)
#     return redirect(posting)


# 