from books.models import Recipie
from rest_framework import serializers


class RecipieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Recipie.objects.create(validated_data)


class RecipieDetailed(serializers.Serializer):
    pass
