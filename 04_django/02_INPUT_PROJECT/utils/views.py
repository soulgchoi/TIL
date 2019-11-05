import requests
from django.shortcuts import render, redirect
from art import *
from decouple import config


def index(request):
    return render(request, 'utils/index.html')


def art(request):
    # html select option 에 다 쓰지 않고 반복문을 돌릴 수 있다.
    fonts = ['3d_diagonal', 'dancingfont', 'lildevil', 'lean']
    return render(request, 'utils/art.html', {
        'fonts': fonts,
    })


def output(request):
    # data 받아보기
    # method="GET" 의 데이터 받기
    # GET method 로 날라온 request(dictionary like)에서 name 이 user-input인 key값 get
    # print(request.POST)
    user_input = request.GET.get('user-input')
    user_font = request.GET.get('user-font')

    if user_input:
        # user_input = 'EMPTY'    
        result = text2art(user_input, font=user_font)
        return render(request, 'utils/output.html', {
            'result': result,
        })
        # return HttpResponse(user_input)
    else:
        return redirect('/utils/art/')

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


def throw(request):
    return render(request, 'utils/throw.html')


def catch(request):
    word = request.GET.get('word')
    headers = {
            'X-Naver-Client-Id': naver_client_id,
            'X-Naver-Client-Secret': naver_client_secret,
    }

    data = {
        'source': 'ko',
        'target': 'en',
        'text': word,
    }

    res = requests.post('https://openapi.naver.com/v1/papago/n2mt', data=data, headers=headers)
    result = res.json()['message']['result']['translatedText']
    
    return render(request, 'utils/catch.html', {
        'result': result,
        'word': word,
        })
