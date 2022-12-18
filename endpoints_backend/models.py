from django.db import models

# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
