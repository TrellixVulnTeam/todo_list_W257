# Generated by Django 2.1.5 on 2019-01-23 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 16, 45, 9, 669642)),
        ),
        migrations.AddField(
            model_name='list',
            name='updated_at',
            field=models.DateTimeField(default=None),
        ),
    ]