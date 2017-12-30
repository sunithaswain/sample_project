# Register your models here.
from django.contrib import admin
from .models import UsersModel,Tasks,genticketing

class UsersAdmin(admin.ModelAdmin):
    list_display= ('username','password','user_role')
admin.site.register(UsersModel, UsersAdmin)

class TaskAdmin(admin.ModelAdmin):
	list_display =('login','supervisor','status','assigned','process')
admin.site.register(Tasks, TaskAdmin)