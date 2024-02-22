"""blogicum URL Configuration."""


from django.urls import include, path

urlpatterns = [
    # Подключаю адреса всех страниц приложения pages.
    path('pages/', include('pages.urls', namespace='pages')),
    # Подключаю адреса всех страниц приложения blog.
    path('', include('blog.urls', namespace='blog')),
]
