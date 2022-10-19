from django.db import models

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
