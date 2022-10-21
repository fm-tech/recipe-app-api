from books.models import Recipie
from rest_framework import serializers


class RecipieSerializer(serializers.ModelSerializer):

    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Recipie
        fields = ["id", "name", "description", "images", "len_name"]

    def get_len_name(self, object):
        return len(object.name)

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

    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "title and description shoud be different"
            )
        else:
            return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value


# class RecipieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#     document = serializers.DictField()

#     def create(self, validated_data):
#         """Creates a new Recipie given validated data"""
#         return Recipie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name")
#         instance.description = validated_data.get("description")
#         instance.active = validated_data.get("active")
#         instance.document = validated_data.get("document")
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError(
#                 "title and description shoud be different"
#             )
#         else:
#             return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value


# class RecipieDetailed(serializers.Serializer):
#     pass
