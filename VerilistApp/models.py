from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from .constants import status_choices, priority_choices
# Create your models here.

class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True) #listName
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Task(models.Model):

    priority = models.CharField(max_length=6, choices=priority_choices)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=50) #Task Name
    list_name =  models.ForeignKey(List, default=True, on_delete=models.CASCADE) #Parent List Name
    status = models.CharField(max_length=10, choices=status_choices)
    taskId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    def __str__(self):
        return self.title