from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # path('', views.index, name='index'),  # /board/ == board:index
    # read 글 목록(list) render
    # path('articles/', views.list, name='list'),
    # comment 와 구분하기 위해
    path('articles/', views.article_list, name='article_list'),
    # read 글 상세(detail) render
    # path('articles/<int:id>/', views.detail, name='detail'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),

    # create 글쓰기(new) render
    # path('articles/new/', views.new, name='new'),
    path('articles/new/', views.new_article, name='new_article'),
    # create 글 저장(create)
    # path('articles/create/', views.create, name='create'),

    # update 글 수정 쓰기(edit) render
    # path('articles/<int:id>/edit/', views.edit, name='edit'),
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),

    # update 글 실제 수정(update)
    # path('articles/<int:id>/update/', views.update, name='update'),

    # delete 글 삭제(delete)
    # path('articles/<int:id>/delete/', views.delete, name='delete'),
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # create comment
    # path('', views.create, name='create'),
    # path('comments/new/', views.new_comment, name='new_comment'),
    # 1:N 종속관계 데이터의 url
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),

    # delete comment
    path('article/<int:article_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment')
]
