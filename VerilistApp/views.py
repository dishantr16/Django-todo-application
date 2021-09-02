from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import request, viewsets, permissions
from django.contrib.auth import authenticate, login as loginUser, logout
from .serializers import ListSerializer, TaskSerializer
from .models import List, Task
from rest_framework import status



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
    return Response(api_urls)


class CheckListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return List.objects.create(user=user)

    def create(self, request, *args, **kwargs):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     authentication_classes = [SessionAuthentication]

#     def get_queryset(self):
#         user = self.request.user
#         return Task.objects.filter(parent_list_user=user)

# class CheckList(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ListSerializer
#     # queryset = List.objects.all()

#     def get_queryset(self):
#         if self.request.user == List.user:
#             return List.objects.all()
#         return List.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    

#     def perform_destroy(self, instance):
#         instance.visible=False
#         instance.save()

# class CheckListView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ListSerializer
    # queryset = List.objects.all()

# @api_view(['GET'])
# def CheckList(request):

#     if request.user.is_authenticated:
#         lists = List.objects.all()
#         serializers = ListSerializer(lists, many= True)
#         return Response(serializers.data)
    
# @api_view(['GET'])
# def CheckListView(request, id):
#     list_view = List.objects.get(id=id)
#     serializer = ListSerializer(list_view, many = False)
    # return Response(serializer.data)
