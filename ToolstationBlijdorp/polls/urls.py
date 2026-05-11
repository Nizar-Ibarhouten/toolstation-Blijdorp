from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter
from .views import Namw

router = DefaultRouter()
router.register(r'Names', BookViewSet)


urlpatterns = [
  path("",views.index2,name="index2"),
  path("login2",views.index3,name="index3"),
  path("name",views.get_name,name="name"),
  path("updateName",views.update_name,name="updateName"),
    path('api', views.all_names, name='api'),
  
]
