# Generated by Django 3.2.7 on 2021-09-02 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='list',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]