from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile, Post, Tag, Category, Comment, Reply, User, Video
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import PostSerializer, videoSerializer
from .form import BlogForm
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView,CreateAPIView,DestroyAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from .permissions import IsOwnerOrReadOnly, IsOwner
# Create your views here.

def new_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user = user , title = title, 
                content = content, image = image
            )
            print(blog_obj)
            return redirect('/add-blog/')
            
            
    
    except Exception as e :
        print(e)
    
    return render(request , 'new blog.html' , context)

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post
    serializer_class = PostSerializer
	
class VideoList(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = videoSerializer

class VideoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Video
    serializer_class = videoSerializer
