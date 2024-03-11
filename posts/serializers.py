from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "username", "create_datetime", "title", "content")
        extra_kwargs = {
            "id": {"read_only": True},
            "create_datetime": {
                "read_only": True,
                "format": "%m-%d-%Y %H:%M:%S",
            },
        }


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "username", "create_datetime", "title", "content")
        extra_kwargs = {
            "id": {
                "read_only": True,
            },
            "username": {
                "read_only": True,
            },
            "create_datetime": {
                "read_only": True,
                "format": "%m-%d-%Y %H:%M:%S",
            },
        }
