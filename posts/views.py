from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post
from posts.serializers import PostSerializer, PostUpdateSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    http_method_names = ["get", "options", "head", "patch", "post", "delete"]

    def get_serializer_class(self):
        return (
            PostUpdateSerializer if self.request.method == "PATCH" else PostSerializer
        )

    def get_object(self):
        pk = self.kwargs.get("pk", "")
        obj = get_object_or_404(self.get_queryset(), pk=pk)

        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def partial_update(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(
            instance=post,
            data=request.data,
            many=False,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
        )
