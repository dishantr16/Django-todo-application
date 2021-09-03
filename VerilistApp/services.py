from .models import List, Task

def get_list_or_404(list_id, user):
    if not list_id:
        return None
    if not user:
        return None
    task = List.objects.get(id=list_id)
    if not task.user == user:
        return None
    return task

def get_task_or_404(task_id, list_id, user):
    if not task_id:
        return None
    if not list_id:
        return None
    tasks = Task.objects.get(id=task_id)
    if not tasks.user == user:
        return None
    return tasks