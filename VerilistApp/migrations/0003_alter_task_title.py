# Generated by Django 3.2.7 on 2021-09-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0002_auto_20210902_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
