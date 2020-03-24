from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categories, Post

admin.site.register(Categories)
admin.site.register(Post)