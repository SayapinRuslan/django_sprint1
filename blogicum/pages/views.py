"""Обработчик страниц."""


from django.shortcuts import render
from django.http import HttpResponse


def about(request) -> HttpResponse:
    """Представление страницы - О проекте."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request) -> HttpResponse:
    """Представление старницы - првила сайта."""
    template = 'pages/rules.html'
    return render(request, template)
