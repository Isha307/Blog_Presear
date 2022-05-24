from django.contrib import admin
from .models import Profile, Post, Tag, Category, Comment, reply
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(reply)