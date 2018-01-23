from django.shortcuts import render
from django.contrib.auth import login as auth_login
# Create your views here.
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from gatewaylogin.models import models,Tasks,genticketing
from .forms import loginform,ticketlogform
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
def gateway_login(request):
    success_message=" "
    print ("login view")
    #form = loginform(request.POST)  
    if request.method == 'POST':  
        form = loginform(request.POST) 
        print ('after post method')      
        password = request.POST.get('password')
        name_user = request.POST.get('name')   
        print (name_user, password,">>>>>>>>>>>>>>>")     
        if form.is_valid():
            user = authenticate(username=name_user,password=password)
            auth_login(request, user)
            #user_id = User.objects.create_user(username=name,password=password)
            success_message = "User successfully created"

        else:
            print('not valid form')
    else:
        print ('else condition')
        form = loginform()
        print()
    return render(request, 'gateway_login.html', {'form':form, 'message':success_message})
def generate_ticket(request):
    success_message=" "
    print ("login view")
    if request.method == "POST":
        form = ticketlogform(request.POST)
        emp_id = request.POST.get('ids')
        desc = request.POST.get('description')
        dead_line_date = request.POST.get('deadline')
        task_type = request.POST.get('ticket_type')
        dep=request.POST.get('department')
        stat=request.POST.get('status')

        if form.is_valid:
            genticketing.objects.create(details=task_type,descripition=desc,
                ids=emp_id,deadline=dead_line_date,Department=dep,status=stat)
            success_message = "Ticket is generated"
        else:
            print ("Not valid")
        
    else:
        form = ticketlogform()
    
    return render(request,'calllog.html',{'form':form, 'message':success_message})
def reporting(request):
   return render(request,'reported.html',{})
