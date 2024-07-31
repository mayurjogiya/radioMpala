from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listen, name='listen'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]