# Generated by Django 3.2.7 on 2021-09-06 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0014_alter_task_list_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_At',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]