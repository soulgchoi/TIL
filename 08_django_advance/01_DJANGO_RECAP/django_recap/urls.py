from django.contrib import admin
from django.urls import path, include  # include 함수로 app url 접근 가능


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('board/', include('board.urls')),
    path('poll/', include('re_poll.urls')),
]
