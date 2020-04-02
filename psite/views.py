from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Categories, Post
from django.views.generic import View, ListView
from django.conf import settings
from pocket import Pocket, PocketException



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

def pocket_reads(request):
    p = Pocket(
        consumer_key=settings.POCKET_CONSUMER,
        access_token=settings.POCKET_ACCESS_TOKEN
    )
    response = p.retrieve(favorite=1, count=200)
    articles=[]
    urls=[]
    for article in response['list']:
        if response['list'][article]['resolved_title'] != '':
            articles.append(response['list'][article]['resolved_title'])
            urls.append(response['list'][article]['resolved_url'])
        mapped  = zip(articles,urls)
    return render(request, 'pocket_reads.html', {'articles':articles, 'urls':urls, "mapped":mapped})