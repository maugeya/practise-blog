from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='assets/')
    body = models.TextField()
