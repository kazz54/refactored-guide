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



def submit(request):
    return render(request, 'prif/crispy_form.html') 
