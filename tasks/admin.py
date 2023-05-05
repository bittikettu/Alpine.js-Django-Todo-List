from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import Task
from .models import UserK

admin.site.register(Task)

admin.site.register(UserK, UserAdmin)