from django.urls import path
from . import views
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views
from .views import (
    indexmicView,
    postMicrobio, 
    checkNickName,
    MicrobioView
)

urlpatterns = [
#    path('admin/', admin.site.urls), list/labaratory/category
#    path('', indexView),
    path('list/microbio/category', views.mic_index, name='mic_index'),
    path('add/microbio/category', views.indexmicView, name='indexmicView'),
    path('post/ajax/miccat', postMicrobio, name = "post_miccat"),
#    path('dashboard', views.dashboard, name='dashboard'),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),

    path("cbv/", MicrobioView.as_view(), name = "friend_cbv")

]