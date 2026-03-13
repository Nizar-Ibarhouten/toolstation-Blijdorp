from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import register

def index2(request):
    
    return render(request,"polls/html/homepage.html")



def index3(request3):
    
    return render(request3,"polls/html/login.html")


def get_name(request):
    username = request.POST.get('name','')
    if request.method == "POST":
        form = register(request.POST.get)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    if request.method == "GET":
        form = register()
    
    return render(request,"name.html",{"form":form})



