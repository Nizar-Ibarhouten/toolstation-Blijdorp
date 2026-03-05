from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index2(request):
   
    return render(request,"polls/html/homepage.html")

