from django.contrib import admin
from django.urls import path, include
from newsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('profile/', views.profile, name='profile'),
    path('', include('newsapp.urls')),
]


