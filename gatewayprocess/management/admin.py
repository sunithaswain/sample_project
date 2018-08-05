# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Schedule,Table_schedule
from django.contrib import admin

# Register your models here.
class Insertdata(admin.ModelAdmin):
	list_display=('projectcode','episode','startdate','enddate','lock')
	search_fields=['episode','projectcode']
admin.site.register(Schedule,Insertdata)
class Tabledata(admin.ModelAdmin):
	list_display=('product_type','startdate','enddate','project','process','episode','lock','schedule_id')
	search_fields = ['product_type','project', 'episode']
# ,'lock')
admin.site.register(Table_schedule,Tabledata)