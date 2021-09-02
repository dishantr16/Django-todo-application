from django.urls import path, include
from rest_framework import routers
from . import views
from .views import CheckListViewSet

# router = routers.DefaultRouter()
# router.register("lists", views.CheckListViewSet)

# app_name = "VerilistApp"

urlpatterns =  [
    path('', views.apiOverview, name='api-overview'),
    path('checklist/', CheckListViewSet.as_view(), name='checklist view'),
    # path("checklist/"),
    
    
    # CheckListViewSet(), name='checklist'),
    # path('checklist/', views.CheckList, name='CheckList'),
    # path('checklist/<id>/', views.CheckListView, name='CheckList View')
]