# Generated by Django 2.1.5 on 2019-01-23 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20190123_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 16, 48, 1, 913408)),
        ),
    ]