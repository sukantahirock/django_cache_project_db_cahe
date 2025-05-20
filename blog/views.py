from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.decorators.cache import cache_page

# Home view with cache (cached for 60 seconds)
@cache_page(60)
def home(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

# Detail view with cache (cached for 120 seconds)
@cache_page(120)
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
