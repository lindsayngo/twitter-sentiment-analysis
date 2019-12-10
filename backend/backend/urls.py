from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout),
    path('feed/', views.feed),
    path('subscribe/', views.subscribe, name = 'main-subscribe'),
    path('unsubscribe/', views.unsubscribe, name = 'main-unsubscribe'),
    path('register/', views.register),
    path('login/', views.login),
    path('analyze/', views.analyze),
    path('', views.feed),
]