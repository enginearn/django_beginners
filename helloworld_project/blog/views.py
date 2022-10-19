from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPosts
# Create your views here.

class BlogListView(ListView):
    model = BlogPosts
    template_name = 'blog/blog_home.html'
    context_object_name = 'blog_posts' # object_list is the default name


class BlogDetailView(DetailView):
    model = BlogPosts
    template_name = 'blog/blog_post_detail.html'
    context_object_name = 'blog_posts' # object is the default name

