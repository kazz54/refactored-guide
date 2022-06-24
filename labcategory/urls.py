from django.urls import path
from . import views
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views
from .views import (
    indexView,
    postLabcategory, 
    checkNickName,
    LabcategoryView
)

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', indexView),
    path('category/labaratory', views.indexView, name='indexView'),
    path('post/ajax/labcat', postLabcategory, name = "post_labcat"),
#    path('dashboard', views.dashboard, name='dashboard'),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),

    path("cbv/", LabcategoryView.as_view(), name = "friend_cbv")

]