import uuid
from django.utils import timezone
from django.db.models import fields
from rest_framework import request, serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('priority', 'description', 'list_name', 'title', 'status',)


class ListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True)
    description = serializers.CharField(max_length=255, required=True)
