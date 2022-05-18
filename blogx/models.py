from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pic')
    bio = models.TextField(max_length=500, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=256, default='new blog')
    content = FroalaField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    is_draft = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

class Tag(models.Model):
    name = models.CharField(max_length=256)

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

class reply(models.Model):
	reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True)
	rep = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
    

