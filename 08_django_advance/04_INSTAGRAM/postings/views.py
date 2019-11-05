from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting, Comment, HashTag
from .forms import PostingForm, ImageForm, CommentForm


@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    # comments = Comment.objects.all()
    # 어차피 posting 이 나가니까 posting.comments.all 로 html 에서 바로 가져올 수 있다
    comment_form = CommentForm()
    is_like = posting.like_users.filter(id=request.user.id).exists()
    return render(request, 'postings/posting_detail.html', {
        'posting': posting,
        # 'comments': comments,
        'comment_form': comment_form,
        'is_like': is_like,
    })


@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'postings/posting_list.html', {
        'postings': postings,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def create_posting(request):
    # image 일단 받기
    images = request.FILES.getlist('file')

    if request.method == 'POST':
        # image 보다 posting 먼저 확인
        posting_form = PostingForm(request.POST)
        # if posting_form.is_valid():
        if posting_form.is_valid() and len(images) <= 5:  # image 5개 까지만 받기
            posting = posting_form.save(commit=False)
            posting.author = request.user
            posting.save()  # 이미 save 되었는데 image 검증 어떻게 하지?
            # posting 이 있어야 id 등등 있음

            # 해시태그
            # content = posting.content
            words = posting.content.split()
            for word in words:
                if word[0] == '#':
                    tag = HashTag.objects.get_or_create(content=word)  # get_or_create 의 return 은 리스트
                    posting.hashtags.add(tag[0])  # 리스트에서 하나 꺼내야함

            for image in images:
                request.FILES['file'] = image
                image_form = ImageForm(files=request.FILES, )
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.posting = posting  # posting 을 save 안하면 id 가 안나와서 이부분 못함
                    image.save()
            return redirect(posting)

        
        # for image in request.FILES.getlist('file'):
        #     # 하나씩 돌면서 FILES 에 image 저장
        #     request.FILES['file'] = image
        #     image_form = ImageForm(files=request.FILES)  # form 류는 request 로 시작하는 객체여야만 사용(저장) 가능
        #     if image_form.is_valid():
        #         image = image_form.save()
        
    else:
        posting_form = PostingForm()
        image_form = ImageForm()
    return render(request, 'postings/posting_form.html', {
        'posting_form': posting_form,
        'image_form': image_form,
    })

# update, delete 는 작성자만 할 수 있게

@login_required
@require_http_methods(['GET', 'POST'])
def update_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    # posting 의 작성자가 요청보낸 user 와 같은가?
    if posting.author == request.user:
        if request.method == 'POST':
            form = PostingForm(request.POST, instance=posting)
            if form.is_valid():
                # posting = form.save(commit=False)
                # posting.author = request.user
                # posting.save()
                # 작성자 채워져 있으니까, 또 쓸 필요없음
                posting = form.save()
                return redirect(posting)
        else:
            form = PostingForm(instance=posting)
    # 작성자와 request.user 가 다를 때
    else:
        return redirect(posting)
    return render(request, 'postings/posting_form.html', {
            'posting_form': form,
        })

@login_required
@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('postings:posting_list')


@login_required
@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user  # comment 의 author 는 요청 보낸 user
        comment.posting = posting  # comment 의 posting 은 위에서 찾아놓은 posting
        comment.save()
    return redirect(posting)


@login_required
@require_POST
def toggle_like(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    user = request.user
    # posting 좋아요 한 유저중에 id 있으면 == 좋아요를 누른 user 라면
    if posting.like_users.filter(id=user.id).exists():  
        posting.like_users.remove(user)
    else:
        posting.like_users.add(user)
    return redirect(posting)
    # 좋아요 버튼도 detail 에서 받아야 함