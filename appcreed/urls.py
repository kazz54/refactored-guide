from . import views
from django.urls import path
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
]