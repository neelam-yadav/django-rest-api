from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, related_name='blogs')
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField(blank=True)
