from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BlogCreateView(CreateView):
    model = BlogPosts
    template_name = 'blog/blog_post_new.html'
    fields = ['title', 'author', 'content']

class BlogUpdateView(UpdateView):
    model = BlogPosts
    template_name = 'blog/blog_post_edit.html'
    fields = ['title', 'content']

class BlogDeleteView(DeleteView):
    model = BlogPosts
    template_name = 'blog/blog_post_delete.html'
    success_url = reverse_lazy('blog_home')
