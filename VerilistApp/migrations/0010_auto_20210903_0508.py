# Generated by Django 3.2.7 on 2021-09-03 05:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0009_alter_list_due_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='creation_date',
        ),
        migrations.RemoveField(
            model_name='list',
            name='due_date',
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(default='Verilist Null Task', max_length=50),
        ),
    ]