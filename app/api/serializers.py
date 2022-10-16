from app.books.models import Recipie
from rest_framework import serializers


class RecipieSerializer(serializers.Serializer):
    class Meta:
        model = Recipie
        # Initialize fields
        fields = ["name", "description", "active", "document", "images"]
        read_only_fields = ["id"]
