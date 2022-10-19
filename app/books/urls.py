from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# views import
from api.views import RecipieListAV, RecipieDetailAV

router = routers.DefaultRouter()


urlpatterns = [
    path("recipie/list", RecipieListAV.as_view(), name="recipie-list"),
    path("recipie/<int:pk>", RecipieDetailAV.as_view(), name="recipie-details"),
    path("recipie/new", RecipieDetailAV.as_view(), name="recipie-details"),
]
