from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^log/', views.login, name='registering'),
    url(r'^profile/',views.profile, name='profiling'),
    url(r'^change_pwd/',views.changingpassword, name='changing'),
    #url(r'^userprofile/(?P<user_id>[\d]+)',views.profiling, name='userprofiles'),
    #url(r'^pass_chnge/',views.changingpassword, name='change_pwd'),
    url(r'^hashpwd/', views.create_new_user, name='content_details'),
    url(r'^out/',views.logoutin, name='logout'),
    url(r'^task_call/',views.taskin, name='tasking'),
    url(r'^generate/',views.gen_ticketing,name='generating'),
    url(r'^integrtion/',views.integrating,name='integrates'),
    url(r'^double_ids/',views.similar_ids,name='similars'),
    url(r'^datainabout/',views.detail_data,name='detai'),
    url(r'^newslist/',views.new_data,name='newli'),
    url(r'^exreading/',views.excel_read,name='reading'),
    url(r'^pc_master/',views.task_read,name='pctasked'),
    url(r'^shotdetail/',views.shotdata,name='shotdetal'),
    url(r'^shotsup/',views.shotsupervesior,name='shotversior'),
    url(r'^getdat/',views.filteringdata,name='shotdetal'),
    url(r'^getdatversion_2/',views.filteringdata_version2,name='shotdetal_v2'),
    url(r'^student_data/',views.ajax_filter_data_studentdetails,name='ajax_student_data'),

    
    url(r'^static/',views.staticdata,name='statdetal'),   

    url(r'^shots_update/',views.update_shots,name='updt'),
    url(r'^reporting/',views.create_projects_episodes,name='episde'),
    url(r'^arstist/',views.assignedshot,name='updteassigned'),
    url(r'^report/',views.reporting,name='reportgen'),
    url(r'^report_popup/',views.reporting_popup,name='report_popup_gen'),
    url(r'^collegedetils/',views.det,name='colid'),
    url(r'^static_data_versionpopup/',views.det_popup,name='colid'),

]