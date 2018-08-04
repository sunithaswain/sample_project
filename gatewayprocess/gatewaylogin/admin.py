# Register your models here.
from django.contrib import admin
from .models import UsersModel,Tasks,genticketing,upload_files,Shots,project,episodes,subjectdetails,assests,creteassestdata,renderdata

class UsersAdmin(admin.ModelAdmin):
    list_display= ('username','password','user_role')
admin.site.register(UsersModel, UsersAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display =('login','supervisor','status','assigned','process')
admin.site.register(Tasks, TaskAdmin)

class Gen(admin.ModelAdmin):
    list_display=('details','descripition','ids','deadline','Department','status','project')
    search_fields = ['Department']
admin.site.register(genticketing,Gen)
