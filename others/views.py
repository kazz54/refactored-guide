from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import OthcatForm
from .models import Othcat

from django.views import View




def indexothView(request):
    user = request.user
    form = OthcatForm()
    othcats = Othcat.objects.filter(otsr=request.user).exclude()
    return render(request, "indexoth.html", {"form": form, "othcats": othcats})

def oth_index(request):
    othcats = Othcat.objects.all()
    return render(request, 'prif/oth_index.html', {'othcats': othcats})


def postOthcat(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = OthcatForm(request.POST)
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
        if Othcat.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new Labcategory
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new Labcategory.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    



class OthcatView(View):
    form_class = OthcatForm
    template_name = "indexoth.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        othcats = Othcat.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "othcats": othcats})

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
