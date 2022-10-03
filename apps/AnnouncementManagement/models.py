from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime, date
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=500, null=True)
    image = models.ImageField()
    post_date = models.DateTimeField(auto_now_add=True)

  