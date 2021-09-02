from django.http import response
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, generics, filters, permissions
from django.contrib.auth import authenticate, login as loginUser, logout
from .serializers import ListSerializer
from .models import List, Task



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


# class CheckList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ListSerializer
#     queryset = List.objects.all()

# class CheckListView(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ListSerializer

#     def get_object(self, queryset=None, **kwargs):
#         list_view = self.kwargs.get(id)
#         return get_object_or_404(List)

@api_view(['GET'])
def CheckList(request):

    if request.user.is_authenticated:
        lists = List.objects.all()
        serializers = ListSerializer(lists, many= True)
        return Response(serializers.data)
    

@api_view(['GET'])
def CheckListView(request, id):
    list_view = List.objects.get(id=id)
    serializer = ListSerializer(list_view, many = False)
    return Response(serializer.data)



