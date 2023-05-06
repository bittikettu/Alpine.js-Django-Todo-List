from django.db import models
import datetime
from django.contrib.auth.models import User, Group, Permission, AbstractUser

class Task(models.Model):
    title = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)
    price = models.BigIntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return f'({self.id}) {self.title} {self.price}€'

class Person(AbstractUser):
    tasks = models.ManyToManyField('Task', through = 'TasksDone', blank = True, default = None)
    pass

class TasksDone(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    done = models.BooleanField(default = False)
    paid = models.BooleanField(default = False)

    class Meta:
        unique_together = [['person', 'task']]

    def finishtask(self):
        self.done = True
        self.date_joined = datetime.date.today()

    def __str__(self):
        return f'{self.person.username} - {self.date} {self.task.title} {self.task.price}€'