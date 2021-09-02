from re import search
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import request, views
from .serializers import ListSerializer, TaskSerializer
from .utils import create_response
from .services import *
from VerilistApp import serializers



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/checklist/',
        'List View': '/checklist/<id>/',
        'Create List': '/checklist/new/',
        'Update List': '/checklist-update/<id>/',
        'Delete List': '/checklist-delete/<id>/',

        'Task': '/checklist/<id>/task/',
        'Task Create': '/checklist/<id>/task/new/',
        'Task Edit': '/checklist/<id>/task/<taskid>'

    }
    create_response(data=api_urls,code=200)


class TaskListViewSet(views.APIView):
    def get(self,request,task_id):
        if not request.user.is_authenticated:
            return create_response(data="User Not Authenticated",code=403)
        taskList = get_list_or_404(task_id,request.user)
        if taskList == None:
            return create_response(data="User Not Allowed to View the List",code=403)
        return create_response(data=taskList.get_details(),code=200)    
    
    def post(self,request):
        if not request.user.is_authenticated:
            return create_response(data="User Not Authenticated",code=403)
        serializer_instance = ListSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return create_response(data=serializer_instance.errors,code=400)
        data = serializer_instance.validated_data;
        user = User.objects.get(id=request.user.id)
        taskList = List.objects.create(name=data.get("name",""),user=user,description=data.get("description","")
        )
        taskList.save()
        return create_response(data=taskList.id,code=200,message="Created Successfully")



            


