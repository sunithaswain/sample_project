# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-15 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=250)),
                ('password', models.CharField(blank=True, max_length=250)),
            ],
        ),
    ]
