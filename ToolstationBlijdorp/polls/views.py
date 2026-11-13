from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .forms import register

from .models import Names, hardwareproducts,hardwareImages
from .forms import UploadImageForm

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
    data = hardwareproducts.objects.all()
    hardwareImages_data = hardwareImages.objects.all()
    h_images = list(hardwareImages_data)
    hardware_list = list(data)
    new_list = []
    h_images_list = []
    for k in h_images:
        h_images_list.append([k.GereedschapImage.name,k.Naam_product_id])
        for i in hardware_list:
            if i.id == k.Naam_product_id:
                new_list.append([i.id,i.Naam,i.Prijs_inc_btw,i.Gewicht,i.Kwantiteit,i.Beschrijving,str(k.GereedschapImage)])
                # print(h_images_list[3][0])

        # for k in h_images_list:
        #     if k[1] == i.id:
        #         print(k[1],i.id)
        #         new_list.append(k[0])

    hardware_dict = {}
    for k,name in enumerate(new_list):
        # k = new_list[k][0]
        hardware_dict[k] = name
        hardware_dict
        print(hardware_dict)
        
        
    
        
    return HttpResponse(json.dumps(hardware_dict),content_type="application/json")

def store_product(request):
    column_names = [field.column for field in hardwareproducts._meta.fields]
    print(column_names)
   
    if request.method == "POST":
        naam = request.POST.get("Naam")
        gewicht = request.POST.get("Gewicht")
        prijs_inc_btw = request.POST.get("Prijs_inc_btw")
        kwantiteit = request.POST.get("Kwantiteit")
        beschrijving = request.POST.get("Beschrijving")

        hardwareproducts(Naam=naam,Gewicht=gewicht,Prijs_inc_btw=prijs_inc_btw,Kwantiteit=kwantiteit,Beschrijving=beschrijving).save()
        product = hardwareproducts.objects.all().values_list('id',flat=True)
        id_list = []
        for product.id in product:
            id_list.append(product.id)
            print(product.id)
            
    return render(request, "homepage.html",{'id_list':product.id})



class NamesCreate(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = NameSerializer


def upload_file(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        latest_id =  hardwareproducts.objects.all().values_list('id',flat=True)
        tool_images = hardwareImages()
        tool_images.Naam_product_id = latest_id.last()
        tool_images.save()
      
        if form.is_valid():
            for filename, file in request.FILES.items():
                name1 = request.FILES[filename].name
            uploaded_img = form.save(commit=False)
            uploaded_img.image_data = form.cleaned_data['GereedschapImage'].file.read()
            tool_images.GereedschapImage_data = uploaded_img.image_data
            print(name1)
            tool_images.GereedschapImage = name1
            tool_images.save()
            # uploaded_img.save()
            return redirect('/')
        else:
            form = UploadImageForm()
        return render(request, 'homepage.html', {'form': form})
    return render(request, 'homepage.html')
    


def Tail_Page(request):
    Tool_images = hardwareImages.objects.all()[1].GereedschapImage

    return render(request, "TailPage.html",{'toolimages' : Tool_images})