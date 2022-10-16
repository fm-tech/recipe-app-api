from ast import Return
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from api.serializers import RecipieSerializer
from books.models import Recipie


@api_view()
@permission_classes((permissions.AllowAny,))
def recipie_list(request):
    recipies = Recipie.objects.all()
    serializer = RecipieSerializer(recipies, many=True)
    return Response(serializer.data)


@api_view()
def recipie_details(request, pk):
    recipie = Recipie.objects.get(pk=pk)
    serializer = RecipieSerializer(recipie)
    return Return(serializer.data)
