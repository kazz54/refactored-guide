from django.urls import path
from . import views
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views
from .views import (
#    indexView,
    postOthcat, 
    checkNickName,
    OthcatView
)

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', indexView),
    path('other', views.oth_index, name='oth_index'),
    path('category/other', views.indexothView, name='indexothView'),
    path('post/ajax/othcat', postOthcat, name = "post_othcat"),
#    path('dashboard', views.dashboard, name='dashboard'),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),

    path("cbv/", OthcatView.as_view(), name = "friend_cbv")

]