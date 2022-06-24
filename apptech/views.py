from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
#from .forms import TechForm


#class TechFormView(FormView):
#    form_class = TechForm
#    success_url = reverse_lazy('success')
#    template_name = 'prif/crispy_form.html'

def tech(request):
    return render(request, 'prif/crispy_form.html') 

#class SuccessView(TemplateView):
#   template_name = 'prif/success.html'