from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('create/', views.create_post, name='create_post'),
    path('contacts/', views.contacts, name='contacts'),
    path('main-info/', views.main_info, name='main_info'),
]