from django.db import models
from django.contrib.auth.models import AbstractUser

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

class UserK(AbstractUser):
    pass
