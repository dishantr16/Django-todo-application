from django.db.models import fields
from rest_framework import serializers
from .models import Task, List

        

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('priority','description','list_name','title','status',) 



class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = List
        fields = ('name','description','due_date','tasks')