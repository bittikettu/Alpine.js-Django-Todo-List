from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group, Permission, AbstractUser
# Register your models here.

from .models import Task
from .models import Person
from .models import TasksDone

#class TasksInline(admin.StackedInline):
#    model = TasksDone
#    extra = 1

# class PersonAdmin(UserAdmin):
#    inlines = (EventsInline,)


#class TaskAdmin(admin.ModelAdmin):
#    inlines = (TasksInline,)


admin.site.register(Task)
admin.site.register(TasksDone)
admin.site.register(Person, UserAdmin)