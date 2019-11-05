from django.urls import path
from . import views  # views 파일과 연결


# 변수 만들거야!
app_name = 'home'


urlpatterns = [
    # path('', views.index),
    # 이름이 index인 이유는 보통 빈 화면을 index라고 해서 # HOST/home//
    path('', views.index, name='index'),
    # 변수 지정해줬으므로 얘는 뭐라고 해도 home 의 index
    # 다시 html 에서 작업할것임
    # path('hi/<str:name>/', views.hi),  # views 안의 함수를 호출할 수 있게 됨 # HOST/home/hi/
    # variable routing 뭐가 들어오든 변수처리 할 것, views.py 에서 인자 추가
    path('guess/', views.guess, name='guess'),
    path('answer/', views.answer, name='answer'),
]
