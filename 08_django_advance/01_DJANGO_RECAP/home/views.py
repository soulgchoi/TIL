from django.shortcuts import render, HttpResponse


def index(request):
    # return HttpResponse('HOME PAGE')
    return render(request, 'home/index.html')  # templates 로 연결할거임


# 뷰 함수 정의하기
# def hi(request, name):  # request 안쓰면 typeerror.. 사실 아무거나 써도 됨
    # return HttpResponse(f'hi {name}')
    # httpresponse 는 유저와 views 를 연결하는 화살표 역할
    # return render(request, 'home/hi.html', {'name': name})
    # hi.html 에 name 은 어떻게 쓰지?
    # key 줘서 html에 {{ key }}
    # html에서 {{ }} 는 출력
    # 출력을 제외한 나머지는 {% %}, for문이나 if문도

def guess(request):
    return render(request, 'home/guess.html')


def answer(request):
    # print(request.GET)
    # POST 요청으로 날린 데이터는 GET으로 받을 수 없음
    # 다 None 나옴
    cnt = 0
    # if request.GET.get('q1') == '0907':
    #     cnt += 1
    # if request.GET.get('q2') == '떡볶이':
    #     cnt += 1
    # if request.GET.get('q3') == 'LG G7':
    #     cnt += 1
    if request.POST.get('q1') == '0907':
        cnt += 1
    if request.POST.get('q2') == '떡볶이':
        cnt += 1
    if request.POST.get('q3') == 'LG G7':
        cnt += 1
    # POST 로 받아야함
    return render(request, 'home/answer.html', {'count': cnt})
