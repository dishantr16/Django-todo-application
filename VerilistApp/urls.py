from django.urls import path

from . import views


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('checklists/', views.TaskListViewSet.as_view()),
    path('checklists/<uuid:list_id>/', views.TaskListDetailViewSet.as_view()),
    path('checklists/new/', views.TaskListViewSet.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserListDetail.as_view()),
    path('checklists/<uuid:list_id>/tasks/', views.TaskView.as_view()),
    path('checklists/<uuid:list_id>/tasks/new/', views.TaskView.as_view()),
]
