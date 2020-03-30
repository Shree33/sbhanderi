from django.contrib import admin
from .models import Categories, Post
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Categories)
admin.site.register(Post, MarkdownxModelAdmin)




