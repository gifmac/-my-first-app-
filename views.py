from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Ife are are you ?")

#add a new file to the ifeprofile directory with the name urls.pt and type the 

from django.conf.urls import url
from .import views
urlpatterns = [url( r"^$", views.index, name="index")]
