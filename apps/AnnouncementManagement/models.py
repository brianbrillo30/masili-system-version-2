from django.db import models
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='announcement-Images')
    post_date = models.DateTimeField(auto_now_add=True, null=True)

  