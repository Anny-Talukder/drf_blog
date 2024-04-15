from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Blog
from .serializer import BlogSerializer
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'list': 'api/blog_list/',
        'Details View': 'api/blog-details/<str:pk>',
        'Create': 'api/blog-create',
        'Update': 'api/blog-update/<str:pk>',
        'Delete': 'api/blog-delete/<str:pk>',

    }
    return Response(api_urls)

@api_view(['GET'])
def blog_list(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogDetails(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)

@api_view(['POST'])            #create
def blogCreate(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def blogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['Delete'])
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response("Blog is successfully deleted!")