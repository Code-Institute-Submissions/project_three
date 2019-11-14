from django.urls import path, include
# from django import HttpResonse, redirect
from . import views

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('register', views.register, name= 'register'),
    path('login', views.login, name='login'),
]