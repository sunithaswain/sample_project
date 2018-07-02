from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# Create your models here.
class Registerform_model(models.Model):
    username=models.CharField(max_length=250 ,blank=True)
    email=models.CharField(max_length=250,blank=True)
    password = models.CharField(max_length=250,blank=True)
    

class UsersModel(AbstractUser):
    user_role = models.IntegerField(blank=True,null=True)

class Tasks(models.Model):
    """This is tasks data model """
    login = models.CharField(max_length=250,blank=True)
    supervisor = models.CharField(max_length=250,blank=True)
    status = models.CharField(max_length=250,blank=True)
    assigned = models.CharField(max_length=250,blank=True)
    process = models.CharField(max_length=250,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    
class genticketing(models.Model):
    details=models.CharField(max_length=250,blank=True)
    descripition=models.CharField(max_length=250,blank=True)
    ids=models.CharField(blank=True,null=True,max_length=250)
    deadline=models.CharField(blank=True,null=True,max_length=250)
    Department=models.CharField(blank=True,null=True,max_length=250)
    status=models.CharField(blank=True,null=True,max_length=250)
    project=models.CharField(blank=True,null=True,max_length=250)

class upload_files(models.Model):
    """ This model is to  save uploading  excel files paths"""
    excel_files=models.FileField(upload_to='documents/')
class Shots(models.Model):
    """This is shots data model """
    shotno=models.CharField(max_length=250,blank=True)
    episode=models.CharField(max_length=250,blank=True)
    projectname=models.CharField(max_length=250,blank=True)
    supervisor=models.CharField(max_length=250,blank=True)
    assigned=models.CharField(max_length=250,blank=True)
    process=models.CharField(max_length=250,blank=True)
    status = models.CharField(max_length=250,blank=True)


# class reports(models.Model):
#    project=models.CharField(max_length=250,blank=True)
#    episode=models.CharField(max_length=250,blank=True)
#    wip=models.CharField(max_length=250,blank=True)
#    complete=models.CharField(max_length=250,blank=True)
#    approved=models.CharField(max_length=250,blank=True)

class project(models.Model):
    project_name = models.CharField(max_length=250, blank=True, null=True)

class episodes(models.Model):
    project_name = models.CharField(max_length=250, blank=True, null=True)
    episodes = models.TextField(max_length=250, blank=True, null=True)
class subjectdetails(models.Model):
    collegename=models.CharField(max_length=250,blank=True)
    branch=models.CharField(max_length=250,blank=True)
    year=models.CharField(max_length=250,blank=True)
class assests(models.Model):
    chars=models.CharField(max_length=200,blank=True)
    props=models.CharField(max_length=200,blank=True)
    sets=models.CharField(max_length=200,blank=True)
    vehicles=models.CharField(max_length=200,blank=True)
class creteassestdata(models.Model):
    assesttypes=models.CharField(max_length=200,blank=True)
    nameofassests=models.CharField(max_length=200,blank=True)
    assestprocess=models.CharField(max_length=200,blank=True)
    processrelated=models.CharField(max_length=200,blank=True)
    descripition=models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now=True)
class renderdata(models.Model):
    layer=models.CharField(max_length=200,blank=True)
    fromframe=models.TextField(max_length=250, blank=True, null=True)
    toframe=models.TextField(max_length=250, blank=True, null=True)
    totalframe=models.TextField(max_length=250, blank=True, null=True)
    prioirty=models.CharField(max_length=200,blank=True)
    renderdepth=models.CharField(max_length=200,blank=True)
    task_ids=models.CharField(max_length=200,blank=True)
