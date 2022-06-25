#from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth import get_user_model
User = get_user_model()


#@login_required
def index(request):
    return render(request, 'prif/index.html') 


@login_required    
def dashboard(request):
    users = User.objects.all()
    return render(request, 'prif/dashboard.html', {'users': users})    