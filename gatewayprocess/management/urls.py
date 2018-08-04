
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create_scheduler/', views.create_schedule, name='c_schedule'),
    url(r'^scheduleview/', views.tableschedule, name='sched'),
    url(r'^filterdat/', views.filterdata, name='data') ,
    url(r'^ajax_filterdat/', views.ajax_filterdata, name='data1'), 
    url(r'^selectdropdowndata/', views.dropdowndata, name='select'),
    url(r'^dropdowndataajax/', views.ajaxdata, name='selectajax'),
    url(r'^time_scheduler/', views.detailed_time_schedule, name='time_schedule'),  
    url(r'^time_scheduler_ajax/', views.ajax_time_schedule, name='ajax_time_schedule_one'),
    url(r'^checking_graph/', views.graph_data, name='graph_detail'),	
    ]
