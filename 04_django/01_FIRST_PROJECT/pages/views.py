from django.shortcuts import render, HttpResponse
import json


def index(request):
    return HttpResponse('Hi django!')


def about(request):
    me = {
        'name': '최솔지',
        'role': 'student',
        'email': 'bssj@com'
    }

    return HttpResponse(json.dumps(me))


# HTML 내보내기
def portfolio(request):
    # 첫번째는 무조건 request, 뒤는 열려는 파일
    return render(request, 'portfolio.html')  # render 가 HTML 내보내는 함수임


def help(request):
    return render(request, 'help.html')

