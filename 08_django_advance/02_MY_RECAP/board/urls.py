from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('article/', views.article_list, name='article_list'),
]
