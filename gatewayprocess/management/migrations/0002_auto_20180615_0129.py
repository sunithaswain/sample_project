# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-15 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='enddate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='startdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='table_schedule',
            name='enddate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='table_schedule',
            name='startdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]