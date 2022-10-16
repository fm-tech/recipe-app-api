from ast import Return
from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.api.serializers import RecipieSerializer
from app.books.models import Recipie


@api_view()
def recipie_list(request):
    recipies = Recipie.objects.all()
    serializer = RecipieSerializer(recipies)
    return Response(serializer.data)


@api_view()
def recipie_details(request, pk):
    recipie = Recipie.objects.get(pk=pk)
    serializer = RecipieSerializer(recipie)
    return Return(serializer.data)

