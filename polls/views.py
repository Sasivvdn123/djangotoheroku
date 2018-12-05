

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
