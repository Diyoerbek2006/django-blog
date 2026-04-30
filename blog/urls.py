from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('articles/', views.articles_page, name='articles'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.about_page, name='contact'),
]
