# Generated by Django 3.2.7 on 2021-09-07 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0015_task_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_At',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
