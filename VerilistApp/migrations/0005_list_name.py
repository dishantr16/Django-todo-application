# Generated by Django 3.2.7 on 2021-09-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0004_auto_20210902_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
