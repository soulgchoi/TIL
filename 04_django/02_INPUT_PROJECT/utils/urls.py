from django.urls import path
from . import views

urlpatterns = [
    # utils/
    path('', views.index),
    path('art/', views.art),
    path('output/', views.output),
    path('throw/', views.throw),
    path('catch/', views.catch)
]
