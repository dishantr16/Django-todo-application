from datetime import datetime, timezone
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import views, generics
from .serializers import ListSerializer, TaskSerializer
from .models import List, Task
from .services import get_list_or_404
from .utils import create_response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/checklist/',
        'List View': '/checklist/<id>/',
        'Create List': '/checklist/new/',
        'Update List': '/checklist-update/<id>/',
        'Delete List': '/checklist-delete/<id>/',
        'Task': '/checklist/<id>/task/',
        'Task Create': '/checklist/<id>/task/new/',
        'Task Edit': '/checklist/<id>/task/<taskid>'

    }
    return Response(api_urls)


class TaskListViewSet(views.APIView):

    def get(self, request):
        checkLists = []
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)
        taskLists = List.objects.filter(user__username=request.user)
        for taskList in taskLists:
            taskListDetails = taskList.get_detail()
            tasks = []
            listTasks = Task.objects.filter(list_name=taskList)
            for task in listTasks:
                tasks.append(task.get_detail())
            taskListDetails["tasks"] = tasks
            checkLists.append(taskListDetails)
        return create_response(data=checkLists, code=200)

    def post(self, request):
        if not request.user.is_authenticated:
            return create_response(data="User Not Authenticated", code=403)
        serializer_instance = ListSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return create_response(data=serializer_instance.errors, code=403)

        data = serializer_instance.validated_data
        user = User.objects.get(id=request.user.id)
        taskList = List.objects.create(name=data.get(
            'name', ''), user=user, description=data.get('description', ''))

        taskList.save()
        return create_response(data=taskList.id, code=200, message="Created Successfully")


class TaskListDetailViewSet(views.APIView):

    def get(self, request, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)

        taskList = get_list_or_404(list_id, request.user)
        if taskList == None:
            return create_response(data="User not allowed to view the list", code=403)
        return create_response(data=taskList.get_detail(), code=200)

    def put(self, request, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)
        serializer_instance = ListSerializer(data=request.data)
        if not serializer_instance.is_valid():
            return create_response(data=serializer_instance.errors, code=403)
        validated_data = serializer_instance.validated_data
        task_list = List.objects.get(id=list_id).first()
        task_list.name = validated_data("name")
        task_list.description = validated_data("description")
        task_list.save(update_fields=['name', 'description'])
        return create_response(data="Success", code=200)

    def delete(self, request, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)

        taskList = get_list_or_404(list_id, request.user)
        taskList.delete()
        return create_response(data="deleted successfully", code=200)


class TaskView(views.APIView):

    def get(self, request, list_id):
        checkLists = []
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)
        task_lists = List.objects.filter(id=list_id)
        for task_list in task_lists:
            if not task_list.user == request.user:
                continue
            task_list_details = task_list.get_detail()
            tasks = []
            list_tasks = Task.objects.filter(list_name=task_list)
            for task in list_tasks:
                tasks.append(task.get_detail())
            task_list_details["tasks"] = tasks
            checkLists.append(task_list_details)
            return create_response(data=checkLists, code=200)

    def post(self, request, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User Not Authenticated", code=403)
        serializer_instance = TaskSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return create_response(data=serializer_instance.errors, code=403)

        validated_data = serializer_instance.validated_data
        tasks = List.objects.get(id=list_id)
        taskList = Task.objects.create(title=validated_data.get('title', ''), description=validated_data.get(
            'description', ''), status=validated_data.get('status', ''), priority=validated_data.get('priority', ''), due_date=validated_data.get('due_date', ''), completed_At=validated_data.get('completed_At', ''))
        taskList.save()
        return create_response(data=taskList.taskId, code=200, message="Created Successfully")


class TaskViewDetail(views.APIView):

    def get(self, request, task_id, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)

        task = Task.objects.get(taskId=task_id)
        if not task.list_name.id == list_id:
            return create_response(data="No task found in the list", code=403)
        return create_response(data=task.get_detail(), code=200)

    def put(self, request, task_id, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)
        serializer_instance = TaskSerializer(data=request.data)
        if not serializer_instance.is_valid():
            return create_response(data=serializer_instance.errors, code=403)
        validated_data = serializer_instance.validated_data
        task = Task.objects.get(taskId=task_id)
        if not task.list_name.id == list_id:
            return create_response(data="No task found in the list", code=403)
        if task.status == 'Completed' and task.status != 'Completed':
            task.completed_At = datetime.now()
        task.priority = validated_data.get("priority")
        task.status = validated_data.get("status")
        task.description = validated_data.get("description")
        task.title = validated_data.get("title")
        task.due_date = validated_data.get("due_date")
        task.completed_At = validated_data.get("completed_At")
        task.save(update_fields=['title', 'priority',
                  'status', 'description', 'due_date', 'completed_At'])
        return create_response(data="Updated Task", code=200)

    def delete(self, request, task_id, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)

        task_list = Task.objects.get(taskId=task_id)
        if not task_list.list_name.id == list_id:
            return create_response(data=" No task found in the list", code=403)
        task_list.delete()
        return create_response(data="deleted successfully", code=200)
