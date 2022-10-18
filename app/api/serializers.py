from books.models import Recipie
from rest_framework import serializers


class RecipieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    document = serializers.DictField()

    def create(self, validated_data):
        """Creates a new Recipie given validated data"""
        return Recipie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.active = validated_data.get("active")
        instance.document = validated_data.get("document")
        instance.save()
        return instance


class RecipieDetailed(serializers.Serializer):
    pass
