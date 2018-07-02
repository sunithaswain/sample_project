# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Schedule(models.Model):
	startdate=models.DateTimeField(auto_now=False,blank=True)
	enddate=models.DateTimeField(auto_now=False,blank=True)
	lock=models.CharField(max_length=250 ,blank=True, null=True)
	projectcode=models.CharField(max_length=250 ,blank=True, null=True)
	episode=models.CharField(max_length=250 ,blank=True, null=True)
class Table_schedule(models.Model):
	startdate=models.DateTimeField(auto_now=False,blank=True)
	enddate=models.DateTimeField(auto_now=False,blank=True)
	project=models.CharField(max_length=250 ,blank=True,null=True)
	process=models.CharField(max_length=250 ,blank=True,null=True)
	product_type=models.CharField(max_length=250 ,blank=True,null=True)
	episode=models.CharField(max_length=250 ,blank=True,null=True)
	lock=models.CharField(max_length=250 ,blank=True, null=True)