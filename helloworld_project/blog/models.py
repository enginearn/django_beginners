from django.db import models
from django.urls import reverse

# Create your models here.
class BlogPosts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    def get_absolute_url(self) -> str:  # new
        # This method should return the url to access a detail record for this blog.
        return reverse("blog_post_detail", args=[str(self.pk)])
