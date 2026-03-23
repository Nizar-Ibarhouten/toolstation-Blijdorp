from django.urls import path

from . import views

urlpatterns = [
  path("",views.index2,name="index2"),
  path("login2",views.index3,name="index3"),
  path("name",views.get_name,name="name"),
  
]
