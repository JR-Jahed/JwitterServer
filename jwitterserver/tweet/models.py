from django.db import models

from user.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=300)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

