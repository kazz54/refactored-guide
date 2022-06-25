from django.urls import path
from . import views
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views
from .views import (
#    indexView,
    postRadcategory, 
    checkNickName,
    RadcategoryView
)

urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', indexView),
    path('radiology', views.rad_index, name='rad_index'),
    path('category/radiology', views.index2View, name='index2View'),
    path('post/ajax/radcat', postRadcategory, name = "post_radcat"),
#    path('dashboard', views.dashboard, name='dashboard'),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),

    path("cbv/", RadcategoryView.as_view(), name = "friend_cbv")

]