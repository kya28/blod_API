from asyncio import mixins

from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Post, Comment
from .pemissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     #queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Post.objects.all()
#         return Post.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=False)
#     def comment(self, request):
#         comments = Comment.objects.all()
#         return Response({'comments': [(c.name, c.body, c.email) for c in comments]})

class PostApiListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PostApiListPagination


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly, )


class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostAPIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         return Response({'posts': PostSerializer(posts, many=True).data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.author = request.user
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT not allowed"})
#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             post = Post.objects.get(pk=pk)
#             post.delete()
#         except:
#             return Response({"error": "Method DELETE not allowed"})
#         return Response({"post delete"})
