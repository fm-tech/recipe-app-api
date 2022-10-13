from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# views import
from .views import recipie_list

router = routers.DefaultRouter()


urlpatterns = [path("recipie/list/", recipie_list, name="recipie-list")]
