# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-29 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gatewaylogin', '0017_creteassestdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='creteassestdata',
            name='descripition',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]