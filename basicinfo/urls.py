from . import views
from django.urls import path
from django.views.generic import TemplateView, View
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
#    path('research/welcome', views.welcome, name='welcome'),
    path('assesiment', views.application, name='application'),
#    path('drafts/', views.post_draft_list, name='post_draft_list'),
#    path('post/<int:pk>/', views.post_detail, name='post_detail'),
#    path('drafts/hist', views.hist_draft_list, name='hist_draft_list'),
#    path('post/<int:pk>/edit/', views.application_edit, name='application_edit'),
#    path('render/pdf/<int:pk>/', views.pdf, name='pdf'),
#    handler404 = 'views.page_not_found_custom'    
#    handler500 = 'views.page_error_found_custom' 
#    path('render/pdf/hist/<int:pk>/', views.pdftwo, name='pdftwo'),
#    path('dashboard1', views.post_index, name='post_index'),
#    path('dashboard1', views.dashboard1, name='dashboard1'),
    
#    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
#    path('profile/books/', TemplateView.as_view(template_name='home.html'), name='book'),
#    path('profile/books/list/', views.book_list, name='book_list'),
#    path('profile/books/index/', views.book_index, name='book_index'),
#    path('profile/books/twolist', views.book_form, name="book-form"),
#    path('profile/books/create/', views.book_create, name='book_create'),
#    path('profile/grants/create/', views.grant_create, name='grant_create'),
#    path('profile/books/<int:pk>/update/', views.book_update, name='book_update'),
#    path('profile/books/<int:pk>/delete/', views.book_delete, name='book_delete'),
#    path('contact', views.contact, name='contact'),
#    path('dashboard', views.dashboard, name='dashboard'),
    
    
]