from django.urls import path
from . import views  # 내 위치에서 views 가져오기

# 이 변수 안쓰면 에러뜸!
# 아무말 안쓸거라도 urlpatterns = [] 만이라도 쓰기
urlpatterns = [
    # <> 고정값 아닌 것의 상징
    # /utils/cube/<정수>/
    path('cube/<int:num>', views.cube),
    # utils/check_int/<정수>/
    path('check_int/<int:num>', views.check_int),
    # pick_lotto/
    path('pick_lotto/', views.pick_lotto),
]
