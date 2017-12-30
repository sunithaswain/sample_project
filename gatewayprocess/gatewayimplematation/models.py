from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
class loginModel(models.Model):
    username=models.CharField(max_length=250 ,blank=True)
    #email=models.CharField(max_length=250,blank=True)
    password = models.CharField(max_length=250,blank=True)
    

# class UsersModel(AbstractUser):
#     user_role = models.IntegerField(blank=True,null=True)


# class Tasks(models.Model):
# 	"""This is tasks data model """
# 	login = models.CharField(max_length=250,blank=True)
# 	supervisor = models.CharField(max_length=250,blank=True)
# 	status = models.CharField(max_length=250,blank=True)
# 	assigned = models.CharField(max_length=250,blank=True)
# 	process = models.CharField(max_length=250,blank=True)
	
# class genticketing(models.Model):
# 	details=models.CharField(max_length=250,blank=True)
# 	descripition=models.CharField(max_length=250,blank=True)
# 	ids=models.CharField(blank=True,null=True,max_length=250)
# 	deadline=models.CharField(blank=True,null=True,max_length=250)
# 	Department=models.CharField(blank=True,null=True,max_length=250)
# 	status=models.CharField(blank=True,null=True,max_length=250)


