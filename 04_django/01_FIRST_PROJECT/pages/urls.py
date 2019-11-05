from django.urls import path
from . import views
# 여기서 views 는 하나밖에 없음!
# pages 는 project 의 urls 에 있으므로, 안써도 됨
urlpatterns = [
    path('', views.index),  # DOMAIN/pages/
    path('about/', views.about),  # DOMAIN/pages/about/
    path('portfolio/', views.portfolio),  # D/pages/portfolio/
    path('help/', views.help),
]
