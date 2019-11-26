"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('feed/', views.feed),
    path('feed/subscribe', views.subscribe, name = 'main-subscribe'),
    path('feed/unsubscribe', views.unsubscribe, name = 'main-unsubscribe'),
    path('feed/filter', views.filter, name = 'main-filter'),
    path('register/', TemplateView.as_view(template_name="register.html"), name="register"),
    path('register/register', views.register),
    path('login/', TemplateView.as_view(template_name="login.html"), name = "login"),
    path('login/login', views.login),
    # url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
]
