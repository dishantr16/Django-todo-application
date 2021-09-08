from .models import List, Task
from django.contrib.auth.models import User
from datetime import date

def get_list_or_404(list_id, user):
    if not list_id:
        return None
    if not user:
        return None
    task = List.objects.get(id=list_id)
    if not task.user == user:
        return None
    return task
