# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaylogin', '0003_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='genticketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=250)),
                ('descripition', models.CharField(blank=True, max_length=250)),
                ('ids', models.IntegerField(blank=True, null=True)),
                ('deadline', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]