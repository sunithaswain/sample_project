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
    url(r'^shots_update/',views.update_shots,name='updt'),
    url(r'^arstist/',views.assignedshot,name='updteassigned'),
    ]