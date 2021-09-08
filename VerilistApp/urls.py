from django.urls import path

from . import views
from . import tasks

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('checklists/', views.TaskListViewSet.as_view()),
    path('checklists/new/', views.TaskListViewSet.as_view()),
    path('checklists/<uuid:list_id>/', views.TaskListDetailViewSet.as_view()),
    path('checklists/<uuid:list_id>/tasks/', views.TaskView.as_view()),
    path('checklists/<uuid:list_id>/tasks/new/', views.TaskView.as_view()),
    path('checklists/<uuid:list_id>/tasks/<uuid:task_id>/', views.TaskViewDetail.as_view()),
    path('sendmail/', tasks.send_mail_to_all, name='sendmail'),
    path('schedulemail/', tasks.schedule_mail, name='schedule mail')
]
