from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

posts = [
    {
        "id": 1,
        "title": "Post 01",
        "content": "Post data",
    },
    {
        "id": 2,
        "title": "Post 02",
        "content": "Post data",
    },
    {
        "id": 3,
        "title": "Post 03",
        "content": "Post data",
    },
    {
        "id": 4,
        "title": "Post 04",
        "content": "Post data",
    },
]


def home_view(request: HttpRequest) -> HttpResponse:
    name = 'Ali Valiyev - Blog Site'
    return render(
        request,
        'home.html',
        context={
            'name': name,
            'posts': posts[-3:]
        },
    )


def blogs_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Blogs Page</h1>')


def blog_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    return HttpResponse('<h1>Blog Detail Page</h1>')
