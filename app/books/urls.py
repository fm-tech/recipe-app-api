from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# views import
from api.views import recipie_list, recipie_post, recipie

router = routers.DefaultRouter()


urlpatterns = [
    path("recipie/list", recipie_list, name="recipie-list"),
    path("recipie/<int:pk>", recipie, name="recipie-details"),
    path("recipie/new", recipie_post, name="recipie-details"),
]
