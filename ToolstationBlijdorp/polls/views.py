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
    content = {}
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name1 = request.POST.get("name")
            name = Names(User_names=name1).save()
            names = Names.User_names

            
            if name1:
                content['name'] = name1
                print("True", names,name1)
            else: 
                print(names,"hierzo",name1)
            
            return render(request, "name.html", {"content":content["name"]})

    # if a GET (or any other method) we'll create a blank form
  
    

    return render(request, "name.html", {"content":content})

