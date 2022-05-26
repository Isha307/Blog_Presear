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
    subcategory = models.ForeignKey('subcategory', on_delete=models.CASCADE, null=True, blank=True)
    is_draft = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)


class likes(models.Model):
    user = models.ForeignKey('Profile', blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

class Video(models.Model):
    title = models.CharField(max_length=256, default='new blog')
    content = FroalaField()
    series = models.IntegerField()
    pub_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog')
    video = models.FileField(upload_to='video')
    author = models.ForeignKey('Profile',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    subtegory = models.ForeignKey('subcategory', on_delete=models.CASCADE, null=True, blank=True)
    is_draft = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)

'''class Company(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='logo')
    description = models.TextField()
    headquartes = models.TextField()
    business_model = models.CharField(max_length=100)
    founding_date = models.DateField()
    employees_number = models.IntegerField()
    CoreTeam = models.TextField()
    facebook = models.TextField(blank=True)
    twitter = models.TextField(blank=True)
    linkedin = models.TextField(blank=True)

class CompanyPost(models.Model):
    post = models.ManyToManyField('Post', blank=True)
    company_name = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)'''

class Tag(models.Model):
    name = models.CharField(max_length=256)

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

class subcategory(models.Model):
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    

class reply(models.Model):
	reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="replies", null=True)
	rep = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

class Bookmark(models.Model):
    user = models.ForeignKey('Profile' , on_delete=models.CASCADE)
    post = models.ManyToManyField('Post', blank=True)

    

