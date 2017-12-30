# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-31 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaylogin', '0002_auto_20171030_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(blank=True, max_length=250)),
                ('supervisor', models.CharField(blank=True, max_length=250)),
                ('status', models.CharField(blank=True, max_length=250)),
                ('assigned', models.CharField(blank=True, max_length=250)),
                ('process', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]