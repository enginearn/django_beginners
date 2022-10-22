from django.urls import path

from .views import (
                    BlogListView,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView,
                    )

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_post_detail'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_post_new'),
    path('blog/<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_post_edit'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_post_delete'),
]
