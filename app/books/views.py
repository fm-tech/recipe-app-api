from django.shortcuts import render
from .models import Recipie
from django.http import JsonResponse

# Create your views here.
def recipie_list(request):
    recipies = Recipie.objects.all()
    data = {"recipies": list(recipies.values())}
    return JsonResponse(data)


def recipie_details(requests, pk):
    recipie = Recipie.objects.get(pk=pk)
    data = {
        "name": recipie.name,
        "description": recipie.description,
        "document": recipie.document,
    }
    return JsonResponse(data)
