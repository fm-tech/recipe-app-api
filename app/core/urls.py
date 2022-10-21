from django.urls import path, include
from rest_framework import routers, serializers, viewsets

# view import
from core.views import MenuListAV

urlpatterns = [path("menus", MenuListAV.as_view(), name="menu-list")]
