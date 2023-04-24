from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here
def index(request):
    posts = Post.published.all()
    return render(request,'blog/post/index.html',{'posts':posts})

def detail(request, year, month, day, post):
    posts = get_object_or_404(Post, slug=post,
                              status='published',
                              publish__year=year,
                              publish__month=month,
                              publish__day=day)
    return render(request, 'blog/post/detail.html',{'post':post})