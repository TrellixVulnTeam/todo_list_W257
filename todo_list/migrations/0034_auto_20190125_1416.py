# Generated by Django 2.1.5 on 2019-01-25 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0033_auto_20190125_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='user',
            new_name='users',
        ),
    ]