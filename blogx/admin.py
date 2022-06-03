from django.contrib import admin
from django.contrib.auth.admin import User
from .models import Profile, Post, Tag, Category, Comment, Reply, subcategory, likes, Bookmark,Video

# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(subcategory)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(likes)
admin.site.register(Video)
admin.site.register(Bookmark)