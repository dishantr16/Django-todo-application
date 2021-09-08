from datetime import date
from django.db.models import fields
from rest_framework import request, serializers
import uuid
from django.contrib.auth.models import User
from .models import Task, List
from .constants import status_choices, priority_choices


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=255, required=True)
    priority = serializers.ChoiceField(choices=priority_choices, required=True)
    status = serializers.ChoiceField(choices=status_choices, required=True)
    due_date = serializers.DateField(required=True)
    completed_At = serializers.DateField(default=date.today)


class ListSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    name = serializers.CharField(max_length=50, required=True)
    description = serializers.CharField(max_length=255, required=True)
