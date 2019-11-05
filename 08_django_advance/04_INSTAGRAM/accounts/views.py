from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout
# 회원가입용 Form, 인증(login)용 Form
from .forms import CustomAuthenticationForm, CustomUserCreationsForm

# 현재 project 에서 사용할 User 모델을 return 하는 함수
# from .models import User
from django.contrib.auth import get_user_model  # 변수랑 유사하지만 더 안전한 방법, AUTH_USER_MODEL 자체를 가져옴
# shell_plus 에서 get_user_model() 해보면 accounts.models.User 꺼내오는 것을 확인할 수 있다
# get_user_model()() 는 비어있는 User (쓰기 좋은 코드는 아님)
User = get_user_model()


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            user = form.save()  # 회원가입
            auth_login(request, user)  # 끝나고 로그인
            return redirect('/')
    else:
        form = CustomUserCreationsForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('/')


@require_GET
def user_page(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_page.html', {
        'user_info': user_info,
    })


def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(User, id=user_id)

    if fan != star:
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)  # star 가 결국 User 객체이기 때문에, user_page 로 잘 감