from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from .constants import status_choices, priority_choices
# Create your models here.


class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default="Verilist Null Task")
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_detail(self):
        return {
            "list_id": self.id,
            "list_name": self.name,
            "user": self.user.username,
            "desc": self.description,
            "created_at": self.creation_date
        }

class AppUser(User):
    user_email = models.EmailField(blank=False)
    user_name = models.CharField(blank=False, verbose_name="username", max_length=100)


class Task(models.Model):

    priority = models.CharField(max_length=6, choices=priority_choices)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, null=True)
    list_name = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=status_choices)
    taskId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_detail(self):
        return {
            "task_id": self.taskId,
            "title": self.title,
            "list_id": self.tasks.id,
            "status": self.status,
            "desc": self.description,
            "created_at": self.creation_date,
            "due_date": self.due_date
        }
