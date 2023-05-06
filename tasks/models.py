from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    price = models.BigIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True, blank=True)
    finished = models.DateTimeField(auto_now_add=True, blank=True)

class UserK(AbstractUser):
    pass
