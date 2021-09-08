from django.http.response import HttpResponse
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from django.contrib.auth import get_user_model
from verilistProject import settings
from celery import shared_task
from django.core.mail import send_mail,EmailMessage
from django.template import Context
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import get_template, render_to_string
from .models import Task
from datetime import date, timezone
from django.db.models import Q

@shared_task(bind=True)
# @receiver(post_save)
def send_mail_func(self, **kwargs):
    users = get_user_model().objects.all()
    for user in users:
        completedTasks = Task.objects.filter(Q(status='Completed')).filter(Q(completed_At=date.today()))
        print(completedTasks)
    message = render_to_string("mail.html",{
    'task': completedTasks
    })
    users = get_user_model().objects.all()
    for user in users:
        mail = EmailMessage(
            subject="Task Summary",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
            reply_to=[settings.EMAIL_HOST_USER]
        )
    mail.content_subtype = "html"
    return mail.send()



def send_mail_to_all(request):
    send_mail_func()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(minute='0', hour='8')
    task = PeriodicTask.objects.create(
        crontab=schedule, name="Schedule_mail_task", task='send_mail_app.tasks.send_mail_func')
    return HttpResponse("Done")
