from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from api.serilizers.core_models import MenuSerializer
from core.models import Menu


class MenuListAV(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
