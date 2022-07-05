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
from django.contrib.auth.models import Group
#from .models import User 
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import RegistrationForm, ProfileForm 
from django.contrib.auth import get_user_model
User = get_user_model()


#class RegistrationView(CreateView):
#    template_name = 'registration/register.html'
#    form_class = RegistrationForm

#    def get_context_data(self, *args, **kwargs):
#        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
#        context['next'] = self.request.GET.get('next')
#        return context

#    def get_success_url(self):
#        next_url = self.request.POST.get('next')
#        success_url = reverse('login')
#        if next_url:
#            success_url += '?next={}'.format(next_url)

#        return success_url
#@login_required
def RegistrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='general')
            user.groups.add(group)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile/profile.html'

    def get_success_url(self):
        if self.request.user.is_staff:
         return reverse('welcome')
        if self.request.user.is_svp:
         return reverse('indexView')
        if self.request.user.is_spo:
         return reverse('index2View')
        if self.request.user.is_rev:
         return reverse('indexmicView')         

    def get_object(self):
        return self.request.user

#@login_required
#def ProfileView(request):
#     if request.user.is_authenticated:
#        if request.user.is_staff:
#         if request.method == "POST":
#          form = ProfileForm(request.POST, request.FILES)
#        if form.is_valid():
#        if user.is_active:
#            application = form.save(commit=False)
#            application.author = request.user
#            application.published_date = timezone.now()
 #           application.modified = auto_now(True)
#            application.save()
#            if user is not None:
        
            # You need to call `login` with `request` AND `user`
#            login(request, user)
#            print("logged in")
#            return HttpResponseRedirect('/')
#    else:
#        return HttpResponseRedirect('/accounts/login/')
#            return redirect('welcome')
#    else:
#        form = ProfileForm()
#    return render(request, 'profile/profile.html', {'form': form})


#login
#def ProfileView(request):
#    if request.user.is_authenticated:
#        if request.user.is_staff:
#            return redirect('staff_dashboard')
#        else:
#            return redirect('user_dashboard')
#    else:
#        if request.method == "POST":
#            username = request.POST.get("username")
#            password = request.POST.get("password")

#            user = auth.authenticate(request,username=username,password=password)

#            if user is not None:
#                if user.is_staff:
#                    auth.login(request,user)
#                    return redirect('staff_dashboard')
#                else:
#                    auth.login(request,user)
#                    return redirect('user_dashboard')
#            else:
#                messages.info(request,"Username or Password is incorrect")
#                return redirect('login')
    
#def ProfileView(request):
#    if request.user.is_authenticated:
#     if request.method == "POST":
#        form = ProfileForm(request.POST, request.FILES)
        
#        if request.user.is_staff:
#          if form.is_valid():
#           application = form.save(commit=False)
#           application.author = request.user
#           application.save()
#    if request.user.is_admin:
#           return redirect('index')
#     else:
#          form = ProfileForm()
#          return render(request, 'prif/crispy_form.html', {'form': form})      
#     else:
#        if request.user.is_active:
#         return redirect('welcome')
@login_required
def welcome(request):
         return render(request, 'prif/crispy_form.html')

    
        

