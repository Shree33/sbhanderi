from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdownx.models import MarkdownxField
from markdown import markdown


class Categories(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.count()


class Post(models.Model):
    subject = models.CharField(max_length=255)
    body = MarkdownxField()
    category = models.ForeignKey(Categories, related_name='topics', on_delete=models.DO_NOTHING)
    last_updated = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))