 
from django.contrib import admin
from django.urls import path
from . import views
from .views import CheckListView, apiOverview, CheckList

urlpatterns =  [
    path('', views.apiOverview, name='api-overview'),
#     path('checklist/', CheckList.as_view(), name='checklist'),
#     path('checklist/id/', CheckListView.as_view(), name='checklist view'),
    path('checklist/', views.CheckList, name='CheckList'),
    path('checklist/<id>/', views.CheckListView, name='CheckList View')
]