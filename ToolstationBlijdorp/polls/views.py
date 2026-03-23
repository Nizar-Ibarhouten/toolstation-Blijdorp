from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import register



from django.views.decorators.csrf import csrf_protect




def index2(request):
    
    return render(request,"polls/html/homepage.html")



def index3(request3):
    
    return render(request3,"polls/html/login.html")

@csrf_protect
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = register(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/name")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = register()
        

    return render(request, "polls/html/name.html", {"form": form})

