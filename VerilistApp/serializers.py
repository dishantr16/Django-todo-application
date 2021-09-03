from django.db.models import fields
from rest_framework import request, serializers
import uuid
from django.contrib.auth.models import User
from .models import Task, List
from .constants import status_choices, priority_choices

class TaskSerializer(serializers.Serializer):
    # taskId=serializers.UUIDField(default=uuid.uuid4)
    # name = serializers.CharField(max_length=50, required=True)
    # description=serializers.CharField(max_length=255)
    # list_name=serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())
    
    class Meta:
        model = Task
        fields = ('priority', 'description', 'list_name', 'title', 'status',)


class UserSerializer(serializers.Serializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')



class ListSerializer(serializers.Serializer):
    id = serializers.UUIDField(default=uuid.uuid4)
    name = serializers.CharField(max_length=50, required=True)
    description = serializers.CharField(max_length=255, required=True)