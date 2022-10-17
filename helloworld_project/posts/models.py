from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

    class Meta:
        db_table = "post"

    def __str__(self) -> str:
        return f"{self.pk} {self.text[:50]}"
