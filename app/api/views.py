from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from api.serilizers.books_models import RecipieSerializer
from books.models import Recipie


class RecipieListAV(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        recipies = Recipie.objects.all()
        serializer = RecipieSerializer(recipies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class RecipieDetailAV(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        try:
            recipie = Recipie.objects.get(pk=pk)
        except Recipie.DoesNotExist:
            # return a 404 response if there is no recipe found
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipieSerializer(recipie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            recipie = Recipie.objects.get(pk=pk)
        except Recipie.DoesNotExist:
            # return a 404 response if there is no recipe found
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecipieSerializer(recipie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET"])
# @permission_classes((permissions.AllowAny,))
# def recipie_list(request):
#     recipies = Recipie.objects.all()
#     serializer = RecipieSerializer(recipies, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes((permissions.AllowAny,))
# def recipie(request, pk):
#     """Retrieve, update, or delete a recipie"""
#     try:
#         recipie = Recipie.objects.get(pk=pk)
#     except Recipie.DoesNotExist:
#         # return a 404 response if there is no recipe found
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = RecipieSerializer(recipie)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = RecipieSerializer(recipie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

#     elif request.method == "DELETE":
#         recipie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["POST"])
# @permission_classes((permissions.AllowAny,))
# def recipie_post(request):
#     serializer = RecipieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
