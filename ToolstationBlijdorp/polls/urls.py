from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter
from .views import Names, NamesCreate

# router = DefaultRouter()
# router.register(r'Names', BookViewSet)


urlpatterns = [
  path("",views.index2,name="index2"),
  path("login2",views.index3,name="index3"),
  path("name",views.get_name,name="name"),
  path("updateName",views.update_name,name="updateName"),
  path('api1/', NamesCreate.as_view(), name='api1'),
  
]
