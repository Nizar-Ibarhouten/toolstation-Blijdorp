from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def index2(request):

    return render(request,"polls/html/homepage.html")



def index3(request3):
   
    return render(request3,"polls/html/login.html")