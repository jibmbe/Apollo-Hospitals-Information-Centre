from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Community/community_posts.html', {'posts': posts})

def index(request):
    return render(request, 'index.html')