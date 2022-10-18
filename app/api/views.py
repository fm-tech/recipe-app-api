from ast import Return
from rest_framework import status
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


@api_view(["GET", "PUT", "DELETE"])
@permission_classes((permissions.AllowAny,))
def recipie(request, pk):
    """Retrieve, update, or delete a recipie"""
    try:
        recipie = Recipie.objects.get(pk=pk)
    except Recipie.DoesNotExist:
        # return a 404 response if there is no recipe found
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RecipieSerializer(recipie)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = RecipieSerializer(recipie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        recipie.delete()
        return Response()


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def recipie_post(request):
    serializer = RecipieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors)
