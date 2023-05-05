from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)

