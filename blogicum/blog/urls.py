"""Пространство адресов сайта."""


from django.urls import path
from . import views

# Определяю пространство имен для приложения blog.
app_name: str = 'blog'

urlpatterns: list = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path(
        'category/<slug:category_slug>/', views.category_posts,
        name='category_posts'
    ),
]
