from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('<int:question_id>/', views.question_detail, name='question_detail')
]
