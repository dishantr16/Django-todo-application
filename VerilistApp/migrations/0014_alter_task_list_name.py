# Generated by Django 3.2.7 on 2021-09-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0013_auto_20210904_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='list_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='VerilistApp.list'),
        ),
    ]