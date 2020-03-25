from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Categories, Post
from django.views.generic import View, ListView




class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'writings.html'

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post':post})

def home(request):
    return render(request, 'home.html')

def about_me(request):
    return render(request, 'about_me.html')

# def writings(request):
#     return render(request, 'writings.html')