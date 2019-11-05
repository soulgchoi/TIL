from django.urls import path
from . import views

# url: /home/
urlpatterns = [
    # 아무말 없으면 index
    path('', views.index),
    path('about/', views.about),
]