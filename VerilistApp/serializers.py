from django.db.models import fields
from rest_framework import serializers
from .models import Task, List

class ListSerializer(serializers.Serializer):
    class Meta:
        model = List
        fields = ('id','name','description','due_date')
        

# class 


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()