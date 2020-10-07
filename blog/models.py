from django.db import models
from django.urls import reverse

# Create your models here.


# blog_post 테이블 
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.pk])