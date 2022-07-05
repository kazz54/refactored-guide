from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import MicrobioForm
from django.utils import timezone
from .models import Microbio

from django.views import View




def indexmicView(request):
#    if request.user.is_rev():
     user = request.user
     form = MicrobioForm()
     microbios = Microbio.objects.filter(mic=request.user).exclude()    
     return render(request, "indexmic.html", {"form": form, "microbios": microbios})


def mic_index(request):
    microbios = Microbio.objects.all()
    return render(request, 'prif/mic_index.html', {'microbios': microbios})

def postMicrobio(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = MicrobioForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)

# BONUS CBV
def checkNickName(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        nick_name = request.GET.get("nick_name", None)
        # check for the nick name in the database.
        if Microbio.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new Labcategory
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new Labcategory.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    



class MicrobioView(View):
    form_class = MicrobioForm
    template_name = "indexmic.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        microbios = Microbio.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "microbios": microbios})

#    def post(self, *args, **kwargs):
        # request should be ajax and method should be POST.
#        if self.request.is_ajax and self.request.method == "POST":
            # get the form data
#            form = self.form_class(self.request.POST)
            # save the data and after fetch the object in instance
#            if form.is_valid():
#                instance = form.save()
                # serialize in new friend object in json
#                ser_instance = serializers.serialize('json', [ instance, ])
                # send to client side.
#                return JsonResponse({"instance": ser_instance}, status=200)
#            else:
                # some form errors occured.
#                return JsonResponse({"error": form.errors}, status=400)

        # some error occured
#        return JsonResponse({"error": ""}, status=400)
