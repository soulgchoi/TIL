"""image_upload URL Configuration

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
from django.urls import path, include

# image 가져오기 위해서
# django 설정 관련 내용
from django.conf.urls.static import static
from django.conf import settings  # MASTER_APP/settings.py 를 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsfeed/', include('sns.urls')),
    # path('media', '/media/ 폴더 안에서 이미지를 찾아라')  =>  이 부분을 static 으로 대체
    path('accounts/', include('accounts.urls')),
]
# urlpateerns 는 리스트이고, static 은 기본적으로 리스트를 반환하기 때문에 리스트 연산으로 표현한다
# image
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



