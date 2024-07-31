from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='Dashboard'),
    path('stores', views.stores, name='Stores'),
    path('show-stores', views.showStores, name='Show Stores'),
    path('add-store', views.addStore, name='add-store'),
    path('add-brand', views.addBrand, name='add-brand'),
    path('managers', views.managers, name='Managers'),
    path('add-manager', views.addManagers, name='add-managers'),
    path('curActive', views.curActive, name='Current Active'),
    path('report', views.report, name='Report')
    
    
    # path('login', views.login, name='login'),
]  