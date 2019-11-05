from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('articles/new/', views.new),  # /board/articles/new/
    path('articles/create/', views.create),  # /board/articles/create
    # Read
    path('articles/', views.index),  # DOMAIN/board/articles/
    path('articles/<int:article_id>/', views.show),  # /board/articles/글번호/
    # Update
    path('articles/<int:article_id>/edit/', views.edit),
    path('articles/<int:article_id>/update/', views.update),
    # Delete
    path('articles/<int:article_id>/delete/', views.delete)  # /board/articles/1/delete/
]
