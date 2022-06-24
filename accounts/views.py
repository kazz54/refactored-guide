from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import User 
from django.utils import timezone
from .forms import RegistrationForm, ProfileForm 



class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url

class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile/profile.html'

    def get_success_url(self):
        return reverse('welcome')

    def get_object(self):
        return self.request.user
    

def welcome(request):
    return render(request, 'prif/crispy_form.html')    
        

