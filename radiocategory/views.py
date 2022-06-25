from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import RadcategoryForm
from .models import Radcategory

from django.views import View




def index2View(request):
    user = request.user
    form = RadcategoryForm()
    radcategorys = Radcategory.objects.filter(radusr=request.user).exclude()
    return render(request, "index2.html", {"form": form, "radcategorys": radcategorys})

def rad_index(request):
    radcategorys = Radcategory.objects.all()
    return render(request, 'prif/rad_index.html', {'radcategorys': radcategorys})


def postRadcategory(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = RadcategoryForm(request.POST)
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
        if Radcategory.objects.filter(nick_name = nick_name).exists():
            # if nick_name found return not valid new Labcategory
            return JsonResponse({"valid":False}, status = 200)
        else:
            # if nick_name not found, then user can create a new Labcategory.
            return JsonResponse({"valid":True}, status = 200)

    return JsonResponse({}, status = 400)
    



class RadcategoryView(View):
    form_class = RadcategoryForm
    template_name = "index2.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        radcategorys = Radcategory.objects.all()
        return render(self.request, self.template_name, 
            {"form": form, "radcategorys": radcategorys})

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
