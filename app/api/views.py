from ast import Return
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from api.serializers import RecipieSerializer
from books.models import Recipie


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def recipie_list(request):
    recipies = Recipie.objects.all()
    serializer = RecipieSerializer(recipies, many=True)
    return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes((permissions.AllowAny,))
def recipie(request, pk):
    if request.method == "GET":
        recipie = Recipie.objects.get(pk=pk)
        serializer = RecipieSerializer(recipie)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = RecipieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
