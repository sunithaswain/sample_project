from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Registerform_model
class loginform(forms.Form):
    Firstname=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)
class changeform(forms.Form):
    oldpassword=forms.CharField(max_length=100)
    newpassword=forms.CharField(max_length=100)

class ticketlogform(forms.Form):
    ticket_type=forms.CharField(max_length=250)
    description=forms.CharField(max_length=250)
    # employee_ids= [
    # ('p6852', 'p6852'),
    # ('p6851', 'p6851'),
    # ('p6875', 'p6875'),
    # ('p6876', 'p6876'),
    # ('p6870', 'p6870')
    # ]
    # ids=forms.CharField(label='Select Id', widget=forms.Select(choices=employee_ids))
    
    ids=forms.CharField(label='Select Id', widget=forms.Select(choices=[
    ('p6852', 'p6852'),
    ('p6851', 'p6851'),
    ('p6875', 'p6875'),
    ('p6876', 'p6876'),
    ('p6870', 'p6870')
    ]))

    deadline=forms.CharField(max_length=250)
    department=forms.CharField(max_length=250)
    status=forms.CharField(max_length=250)


class ExcelUploadForm(forms.Form):
    myuploadfile=forms.FileField()
