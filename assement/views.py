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
from django.urls import reverse_lazy
from .models import Assesment
#from apprimstwo import Histsearch
#from apprimstwo.models import Histsearch 
from .forms import ApplicationForm
#from .render import Render
from django.contrib.auth import get_user_model
User = get_user_model()



#def dashboard(request):
#    return render(request, 'profile/dashboard.html')



#@login_required
#def welcome(request):
#    return render(request, 'profile/welcome.html')    

#@login_required
def index(request):
    return render(request, 'profile/welcome_index.html')    
    
#class application(UpdateView):
#    model = Research
#    fields = ['research_title', 'research_introduction', 'research_broad_objectives', 'research_specific_objectives', 'location_of_Study', 'location_type', 'research_sector_Category', 'research_full_proposal'  ]
#    template_name = 'profile/research.html'

#    def get_success_url(self):
#        return reverse('dashboard')

#    def get_object(self):
#        return self.request.user    
@login_required
def application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.author = request.user
#            application.published_date = timezone.now()
 #           application.modified = auto_now(True)
            application.save()
            return redirect('dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'profile/assessiment.html', {'form': form})

#@login_required
#def application_edit(request, pk):
#    post = get_object_or_404(Research, pk=pk)
#    if request.method == "POST":
#        form = ApplicationForm(request.POST, request.FILES, instance=post)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
            # time update
#            post.published_date = timezone.now()
#            post.published_date = timezone.now()
#            post.modified = auto_now(True)
#            post.save()
#            return redirect('perhist',)
#    else:
#        form = ApplicationForm(instance=post)
#    return render(request, 'profile/research.html', {'form': form})
    
#@login_required    
#def post_index(request):
#    posts = Research.objects.filter(author=request.user, published_date__isnull=True).order_by('created_date')
#    posts = Research.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#    return render(request, 'blog/post_index.html', {'posts': posts})
#@login_required  
#def post_draft_list(request):
#    posts = Research.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#    posts = Research.objects.filter(author=request.user, published_date__isnull=True).order_by('created_date')
#    return render(request, 'blog/post_draft_list.html', {'posts': posts })

#    posts = Research.objects.filter(submitted=True).order_by('created_date')
#    return render(request, 'blog/post_draft_list.html', {'posts': posts })    
#@login_required    
#def post_detail(request, pk):
#    post = get_object_or_404(Research, pk=pk)
    
#    context = {"post": post}
#    return render(request, 'blog/post_detail.html', context)

         
@login_required
def dashboard(request):
    user = request.user
    user_posts = Assesment.objects.filter(author=request.user, published_date__isnull=True).order_by('-created_date')
#    comments = user.comments.all()
 #   user_posts = Research.objects.filter(author=request.user, published_date__lte=timezone.now()).order_by('-published_date')

    template = 'profile/dashboard.html'
    context = {
    
    "posts": user_posts
    
  }

    return render(request, template, {'user_posts':user_posts, 'user': user})    




#class Pdf(View):

#def pdf( request):
#    research_posts = Research.objects.filter(author=request.user, published_date__isnull=True).order_by('-created_date')
#    today = timezone.now()
#    params = {
#        'today': today,
#        'research_posts': research_posts,
#        'request': request
#        }
#    return Render.render('profile/pdf.html', params)

#def pdf(request, pk):
#    research_posts = get_object_or_404(Research, pk=pk)
    
#    today = timezone.now()
#    params = {
#        'today': today,
#        'research_posts': research_posts,
#        'request': request
#        }
#    return Render.render('profile/pdf.html', params)

#def pdftwo(request, pk):
#    histsearch_posts = get_object_or_404(Histsearch, pk=pk)
    
#    today = timezone.now()
#    params = {
#        'today': today,
#        'histsearch_posts': histsearch_posts,
#        'request': request
#        }
#    return Render.render('profile/pdftwo.html', params)






# dashboard test
#def dashboard1(request):
#    user = request.user
    
#    user_posts = Research.objects.filter(author=request.user).order_by('-published_date')

#    template = 'blog/dashboard.html'
#    context = {
    
#    "posts": user_posts
    
#  }

#    return render(request, template, {'user_posts':user_posts, 'user': user})    