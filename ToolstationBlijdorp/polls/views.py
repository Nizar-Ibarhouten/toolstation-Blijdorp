from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import register

from .models import Names

from django.views.decorators.csrf import csrf_protect




def index2(request):
    
    return render(request,"homepage.html")



def index3(request3):
    
    return render(request3,"login.html")


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = Names().User_names
            if name == "":
    
                print("True", name)
            else: 
                print(name,"hierzo")
            
            return HttpResponseRedirect("/name")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = register()
        Imam = "Mohamed"

    return render(request, "name.html", {"value": Imam})

