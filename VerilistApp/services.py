from .models import List


def get_list_or_404(taskid,user):
    if not taskid:
        return None
    if not user:
        return None
    task = List.objects.get(id=taskid)
    if not task.user == user:
        return None
    return task              