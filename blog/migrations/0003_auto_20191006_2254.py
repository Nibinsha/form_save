# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-06 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191005_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]