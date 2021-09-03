from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import views, generics
from .serializers import ListSerializer, TaskSerializer, UserSerializer
from .models import List, Task
from .services import get_list_or_404
from .utils import create_response
from .permissions import IsOwnerOrReadOnly



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
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)

        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)

        return create_response(data=serializer.data, code=200)

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

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class TaskListDetailViewSet(views.APIView):

    # permission_classes = (IsOwnerOrReadOnly,)

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

        taskList = get_list_or_404(list_id, request.user)
        serializer_instance = ListSerializer(taskList, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return create_response(serializer_instance.data)
        return create_response(serializer_instance.errors, code=403)

    def delete(self, request, list_id):
        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)

        taskList = get_list_or_404(list_id, request.user)
        taskList.delete()
        return create_response(data="deleted successfully", code=200)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskView(views.APIView):

    def get(self, request, format=None):

        if not request.user.is_authenticated:
            return create_response(data="User is not authenticated", code=403)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        lists = List.objects.all()
        serializer2 = ListSerializer(lists, many=True)
        return create_response({'tasks': serializer.data, 'Lists': serializer2.data}, code=200)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return create_response(data="User Not Authenticated", code=403)
        serializer_instance = TaskSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return create_response(data=serializer_instance.errors, code=403)

        data = serializer_instance.validated_data
        user = User.objects.get(id=request.user.id)
        taskList = Task.objects.create("""fetch the task details""")

        taskList.save()
        return create_response(data=taskList.id, code=200, message="Created Successfully")

