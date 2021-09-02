from django.urls import path, include
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register("lists", views.CheckListViewSet)

# app_name = "VerilistApp"

urlpatterns =  [
    path('', views.apiOverview, name='api-overview'),
    path("checklists/<uuid:task_id>/",views.TaskListViewSet.as_view()),
    path("checklists/new/",views.TaskListViewSet.as_view())

]