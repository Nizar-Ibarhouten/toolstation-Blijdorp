from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import register

from .models import Names

from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response

from rest_framework import generics
from .serializers import NameSerializer
from django.core import serializers
import json
def index2(request):
    
    return render(request,"homepage.html")



def index3(request3):
    
    return render(request3,"login.html")

def update_name(request4):
    alle_namen = list(Names.objects.all())
    x = Names.objects.all()[1]
    print(x,"hoena")
    x.User_names = "Newgate"
    x.save()
    return render(request4,"updateName.html",{"alle_namen": alle_namen})

def all_names(request22):
    Namen = list(Names.objects.all())
    
    return Response({"Content":Namen})



def get_name(request):
    
    content = {}
    names2 = list(Names.objects.all())
    
    for i in names2:
        print(i)
        
   
    if request.method == "POST":
       
        form = register(request.POST)
        
        if form.is_valid():
            name1 = request.POST.get("name")
            name = Names(User_names=name1).save()
            names = list(Names.objects.all())
    
            if name1:
                content['name'] = name1
                print("True", names,name1)
            else: 
                print(names,"hierzo",name1)
            
            return render(request, "name.html", {"content":names})
     

    return render(request, "name.html", {"content":names2})

def return_json(request):
    name = "hallo there"
    foos = Names.objects.all()
    data = serializers.serialize('json', foos)
    return HttpResponse(data,content_type="application/json")
    

def return_products(request):
    data = [{
        "name" : "bahco hamer",
        "price": "20.99",
        "weight": "250gr",
        "quantity": "5"
    },
    {"name" : "milwakee boor machine",
        "price": "199.00",
        "weight": "3 kg",
        "quantity": "3"
    },{
        
        "name" : "knipex waterpomptang",
        "price": "30.99",
        "weight": "300gr",
        "quantity": "10"}]
    return HttpResponse(json.dumps(data),content_type="application/json")


class NamesCreate(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = NameSerializer


def Tail_Page(request):
    
    return render(request, "TailPage.html")