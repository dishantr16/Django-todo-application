from django.contrib import admin
from .models import List, Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskId','title','description','status')

class ListAdmin(admin.ModelAdmin):
    list_display = ('id','name','description')

admin.site.register(List, ListAdmin)
admin.site.register(Task, TaskAdmin)