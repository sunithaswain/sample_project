# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-05 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_table_schedule_schedule_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table_schedule',
            name='schedule_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
