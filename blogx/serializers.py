from rest_framework import serializers
from .models import Profile, Post, Tag, Category, Comment, Reply, User, Video
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
      
class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
