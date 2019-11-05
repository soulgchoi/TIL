from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
# 인증용 form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# login 
from django.contrib.auth import login as auth_login, logout as auth_logout  # 아래에서 이름이 겹쳐 재귀함수처럼 되므로 이름 바꿈


@require_http_methods(['GET', 'POST'])
def signup(request):  # new_article 과 같은 구조
    # 사용자가 회원가입 할 데이터를 보냈다는 뜻
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # 실패하면 form 은 잘못됐다 는 데이터를 가지고 else 로 이동한다.
        if form.is_valid():
            user = form.save()
            return redirect('sns:posting_list')
        # else:
        #     # 틀린 상태인 form 을 돌려주는 코드
        #     return render(request, 'accounts/signup.html', {
        #         'form': form,
        #     })
    else:  # 사용자가 회원가입 HTML 을 달라는 뜻
        form = UserCreationForm()
        # 완전히 새로운 form(비어있는) 을 가져가는 코드
        # return render(request, 'accounts/signup.html', {
        #     'form': form,
        # })
    return render(request, 'accounts/signup.html', {
            'form': form,
        })


@require_http_methods(['GET', 'POST'])
def login(request):
    # login 한 사람이 또 하지 않도록
    if request.user.is_authenticated:  # 사용자가 login 한 상태라면,
        return redirect('sns:posting_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)  
        # form = AuthenticationForm(request.COOKIES, request.POST) 
        # request 를 첫 번째 인자로 받는건 login 만(base modelform 이 그렇게 짜여있음)
        if form.is_valid():
            # login(request, form.get_user())
            # auth_login 은 알아서 쿠키랑 세션을 써서 또 로그인하지 않게 해줌
            auth_login(request, form.get_user())
            return redirect('sns:posting_list')  # return 값 HttpResponse
            # cookie 저장되는 것 보기, 여기서 말고 form 에서 가능
            # response = redirect('sns:posting_list')
            # response.set_cookie(key='nickname', value='coat', max_age=5)  # set_cookie 는 return 없음 (mutable)
            # return response
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    auth_logout(request)
    return redirect('sns:posting_list')
# logout 은 브라우저에서 쿠키를 없애주는 역할
