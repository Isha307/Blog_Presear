from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import PostList, PostDetail, VideoList, VideoDetail

urlpatterns = [
    path('new_blog',views.new_blog, name='newblog'),
    path('posts', PostList.as_view()),
    path('postdetail/<int:pk>', PostDetail.as_view()),
    path('videos', VideoList.as_view()),
    path('videodetail/<int:pk>', VideoDetail.as_view()),
   

]
