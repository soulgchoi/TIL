"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include 써야 포워딩
# from . import views
# . 은 내 위치
# from pages import views
# from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index)  # 연결
    # 반복과 네임스페이스 겹침을 해결하기 위해
    path('pages/', include('pages.urls')),
    # path('pages/', views.index),  # 보통 뭐 안붙으면 index
    # path('pages/about/', views.about),  # 항상 url 뒤에 / 써주기
    # pages 의 url 에 연결했으므로 여기서는 없앰
    # pages 에 도달했으면, 저쪽으로 보내라는 의미
    # path('test_app/test_view/', views.test_view)
    path('utils/', include('utils.urls'))
]
