# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-30 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaylogin', '0018_creteassestdata_descripition'),
    ]

    operations = [
        migrations.AddField(
            model_name='creteassestdata',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]