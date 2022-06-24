from . import views
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
#    path('profile/passport/', views.ProfilePassportView.as_view(), name='passport'),
    path('equipment/', views.ProfileView.as_view(), name='profile'),
    path('equipment/category', views.welcome, name='welcome'),
#    path('profile/education/', views.ProfileEducationView.as_view(), name='education'), 
#    path('profile/address/', views.ProfileAddressView.as_view(), name='address'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
]