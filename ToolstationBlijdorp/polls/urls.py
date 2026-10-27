from django.urls import path

from . import views
from rest_framework.routers import DefaultRouter
from .views import Names, NamesCreate

# router = DefaultRouter()
# router.register(r'Names', BookViewSet)


urlpatterns = [
  path("index2",views.index2,name="index2"),
  path("login2",views.index3,name="index3"),
  path("name",views.get_name,name="name"),
  path("updateName",views.update_name,name="updateName"),
  path('api1/', NamesCreate.as_view(), name='api1'),
  path("return_json",views.return_json,name="nana"),
  path("",views.Tail_Page,name="Home"),
  path("products",views.return_products,name="mid2"),
  path("storeProduct", views.store_product,name="storeProduct")
]
