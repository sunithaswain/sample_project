# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-01 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaylogin', '0014_tasks_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='genticketing',
            name='project',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
