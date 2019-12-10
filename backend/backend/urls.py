from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .main import views
from backend.main.views import LineChartJSONView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout),
    path('feed/', views.feed),
    path('subscribe/', views.subscribe, name = 'main-subscribe'),
    path('unsubscribe/', views.unsubscribe, name = 'main-unsubscribe'),
    # path('filter/', views.filter, name = 'main-filter'),
    path('register/', views.register),
    path('login/', views.login),
    path('analyze/', views.analyze),
    path('line_chart/json/', LineChartJSONView.as_view(), name='line_chart_json'),
    path('', views.feed),
]