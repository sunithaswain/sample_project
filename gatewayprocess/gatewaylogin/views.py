from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import UsersModel,models,upload_files,Tasks,Shots,genticketing
from .forms import loginform,changeform,ticketlogform,ExcelUploadForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as signout 
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.conf import settings
from xlrd import open_workbook
import os
def login(request):
    ''' Login '''

    error_message = ""
    print ("login view")
    if request.method == 'POST':
        form = loginform(request.POST)  
        print ('after post method')      
        password = request.POST.get('password')
        name = request.POST.get('Firstname')   
        print (name, password)     
        if form.is_valid():
            print ('form is valid')
            user = authenticate(username=name,password=password)        
            print ("valid")           
                          
            auth_login(request, user)
            # auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            user_id = UsersModel.objects.filter(username=name)
            print (user_id)
            for i in user_id:
                if i.user_role == 1:
                    print ('supervisor|upper')
                    # redirect('profiling')                    
                    return HttpResponseRedirect("/process/profile")
                elif i.user_role == 2:
                    print ('artist|upper')
                    # redirect('profiling')
                    return HttpResponseRedirect("/process/profile")                     
                elif i.user_role == 3:
                    print ('developer|upper')
                    # print({{i.email}})
                    return HttpResponseRedirect("/process/profile")
               
                else:
                    return HttpResponseRedirect("/process/profile")                  
            
            # else:
            #     error_message = "User Not found"
            #     print ("User not found")
                      
    else:
        print ('else method')
        form = loginform()
    # return render(request, 'login.html', {'form': form, 'error_message':error_message,})
    return render(request, 'integration_login.html', {'form': form, 'error_message':error_message,})

@login_required(login_url='/process/log/')
def profile(request): 
    print (request.user.username)   
    user_id = UsersModel.objects.filter(username=request.user.username)
    return render(request, 'profile.html', {'data':user_id})
def create_new_user(request):
    users = UsersModel.objects.create(username='1800',user_role=1,email="appalbudda@gmail.com",
        first_name="aneesgadu")
    users.set_password("gateway@123")
    users.save()
    # var = UsersModel.objects.all()
    # for i in var:
    #     data=UsersModel.objects.get(username=i.username)


    #     data.set_password("gateway@143")
    #     data.save()
    return HttpResponse('user created or updated')

@login_required(login_url='/process/log/')
def changingpassword(request):
    print (request.user.id)
    print (request.user.username)

    error_message = ""
    if request.method == 'POST':
        form = changeform(request.POST)
        user_name = request.POST.get('oldpassword')
        password = request.POST.get('newpassword')
        # request.POST['password']
        if form.is_valid():    
            # User.objects.get(username='john')        
            user=UsersModel.objects.get(username=request.user.username)
            # u.set_password('new password')
            user.set_password(password)
            
            user.save()
            error_message = "paasword changed successfully"
    else:
        form=changeform()
    return render(request, 'changepass.html', {'msge':error_message})

    #     print ('else condition')
    #     form = Registerform()
    #     print()
    # return render(request, 'login.html', {'form':form, 'message':success_message})
@login_required(login_url='/process/log/')
def logoutin(request):

    signout(request)
    return redirect('/process/log/')
@login_required(login_url='/process/log/')    
def taskin(request):            
    user = Tasks.objects.all()
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    list1 = ['STATUS','ACCEPTED','WIP', 'COMPLETE']
    print("Task successfully created")
    list2 = ['ASSIGNED','p6852','p6851','p6857', 'p6855']
    print("Task successfully created")
    if request.method == 'GET':
        print ('tasking')
        print (request.GET)

        getval=request.GET.get('check_this')        
        iddata=request.GET.get('user_id')
        assdata=request.GET.get('assign_dat')
        # print (getval,iddata),("<<<<<<<<<<<<")
        print (assdata)

        update_data = Tasks.objects.filter(login=iddata).update(status=getval,assigned=assdata)

        print('task data updated')
        # to_update = TestModel.objects.filter(id=2).update(name='updated_name', key=new_key)
    else:
        return render(request,'task.html',{'details':user,'status':list1,'assigned':list2}) 

        
    return render(request,'task.html',{'details':user,'status':list1,'assigned':list2}) 
def gen_ticketing(request):            
    # user = genticketing.objects.all()
    success_message = ""
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
    
    return render(request,'raiseticket.html',{'form':form, 'message':success_message})
def integrating (request):
    return render(request, 'index.html')
def similar_ids (request):
    print ('my ticketsviews')
    pro=genticketing.objects.filter(ids=request.user.username)
    print(pro,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    list1 = ['STATUS','ACCEPTED','WIP', 'COMPLETE']
    
    if request.method == 'GET':
        print ('tasking')
        statdata=request.GET.get('status_id')
        statid=request.GET.get('t_id')
        print(">>>>>>",statdata)
        update_data = genticketing.objects.filter(id=statid).update(status=statdata)
    #     getval=request.GET.get('check_this')        
    #     iddata=request.GET.get('user_id')
    #     assdata=request.GET.get('assign_dat')
    #     # print (getval,iddata),("<<<<<<<<<<<<")
    #     print (assdata)     
    #     update_data = Tasks.objects.filter(login=iddata).update(status=getval,assigned=assdata)

    #     print('task data updated')
    #     # to_update = TestModel.objects.filter(id=2).update(name='updated_name', key=new_key)
    else:
        return render(request,'my_tickets.html',{'ids_process':pro, 'status':list1})

    

        
    return render(request, 'my_tickets.html',{'ids_process':pro,'status':list1})
def detail_data(request):
    print(">>>>>>>>>>>>")
    return render(request, 'aboutdetail.html',{})
def new_data(request):
    print(">>>>>>>>>>>>")
    return render(request, 'news_detail.html',{})

'''def excel_read(request):
     #Exce data feeding into database model
    if request.method=="GET":
        sheet_name=request.GET.get('status')
        model_cols = []
        wb = open_workbook(os.path.join(settings.MEDIA_ROOT, "data.xlsx"))
        if sheet_name == "create tasks":
            tasks = wb.sheet_by_name(sheet_name)        
            print "tasks condition"
            print tasks
            for row in range(tasks.nrows):                
                print "inside sheet"
                number_of_rows = tasks.nrows
                number_of_columns = tasks.ncols
                print number_of_columns
                print number_of_rows
                for column in range(tasks.ncols):
                    # if tasks.cell(row,column).value == value:
                    print "after column condition"
                    # print row, column
                    value  = (tasks.cell(row,column).value)
                    print value 

                items = []
                rows = []

                # for row in range(1, number_of_rows):
                #     values = []
                #     for col in range(number_of_columns):
                #         value  = (sheet.cell(row,col).value)
                        
                #         try:
                #             value = str(int(value))
                #         except ValueError:
                #             pass
                #         finally:
                #             values.append(value)
                #     print 'list of data',values
                #     print values[1], values[2],values[3],values[4]
                    
                #     users = UsersModel.objects.create(username=values[2],user_role=values[4],email=values[3], first_name=values[1])
                #     users.set_password("gateway@123")
                #     users.save()                

                return HttpResponse("tasks successfully inserted")
        elif sheet_name == "create shots":
            shots = wb.sheet_by_name(sheet_name)
        print sheet_name
    else:
        print settings.MEDIA_ROOT

        # model_cols = []
        # wb = open_workbook(os.path.join(settings.MEDIA_ROOT, "data.xlsx"))
        # for sheet in wb.sheets():
        #     number_of_rows = sheet.nrows
        #     number_of_columns = sheet.ncols
        #     print number_of_columns
        #     print number_of_rows
        #     items = []
        #     rows = []

        #     for row in range(1, number_of_rows):
        #         values = []
        #         for col in range(number_of_columns):
        #             value  = (sheet.cell(row,col).value)
        #             # value = str(int(value))
        #             # values.append(value)
        #             try:
        #                 value = str(int(value))
        #             except ValueError:
        #                 pass
        #             finally:
        #                 values.append(value)
        #         print 'list of data',values
        #         print values[1], values[2],values[3],values[4]
                
        #         users = UsersModel.objects.create(username=values[2],user_role=values[4],email=values[3], first_name=values[1])
        #         users.set_password("gateway@123")
        #         users.save()
                

        #     return HttpResponse("data successfully inserted")
    return HttpResponse("excel feeding")'''
def excel_read(request):
    """ Exce data feeding into database model """
    # ss = UploadExcelFile.objects.all()
    # file_path = ''
    # for i in ss:
    #     file_path = ss.excel_upload_file_path
    # print "$$$$$$",file_path
    #files=upload_files.objects.all()
    if request.method=="GET":
        # getstatus=request.GET.get('status')
        sheet_name=request.GET.get('status')
        
        model_cols = []
        wb = open_workbook(os.path.join(settings.MEDIA_ROOT, "documents/data.xlsx"))
        if sheet_name == "create tasks":
            tasks = wb.sheet_by_name(sheet_name)        
            print "tasks condition"
            print tasks
            for row in range(1, tasks.nrows):                
                # print "inside sheet"
                # number_of_rows = tasks.nrows
                # number_of_columns = tasks.ncols
                # print number_of_columns
                # print number_of_rows
                values = []
                for column in range(tasks.ncols):                    
                    value  = (tasks.cell(row,column).value)                    
                    values.append(value)
                print values
                # [1.0, u'sunita', u'p6850', u'assigned', u'secondary']
                tasks_creatio = Tasks.objects.create(login=values[0],supervisor=values[1],status=values[3], assigned=values[2],process=values[4])
                print "tasks created"
                

                # write model create code here , already we implemented copy here
                
        elif sheet_name == "create shots":
            print "shots condition"
            shots = wb.sheet_by_name(sheet_name)        
            
            for row in range(1, shots.nrows):                
                print "inside sheet"
                number_of_rows = shots.nrows
                number_of_columns = shots.ncols                
                values = []
                for column in range(shots.ncols):                    
                    value  = (shots.cell(row,column).value)                    
                    values.append(value)
                print values
                shots_insert = Shots.objects.create(shotno=int(values[0]),episode=int(values[1]),projectname=values[2],supervisor=int(values[3]),assigned=values[4],process=values[5])

                print "shots created"
            # files=upload_files.objects.create()
            # getstatus=request.GET.get('status')
            # tasks = wb.sheet_by_name(sheet_name)
        elif sheet_name == "create Render":
            print "Render condition"
            Render = wb.sheet_by_name(sheet_name)        
            
            for row in range(1, render.nrows):                
                print "inside sheet"
                number_of_rows = render.nrows
                number_of_columns = render.ncols                
                values = []
                for column in range(render.ncols):                    
                    value  = (render.cell(row,column).value)                    
                    values.append(value)
                print values
                render_insert = render.objects.create(render=(values[0]),shot=int(values[1]),name=values[2])

                print "render created"     
        else:
            print "else"
            pass
    # print settings.MEDIA_ROOT
    # model_cols = []
    # wb = open_workbook(os.path.join(settings.MEDIA_ROOT, "data.xlsx"))
    # for sheet in wb.sheets():
    #     number_of_rows = sheet.nrows
    #     number_of_columns = sheet.ncols
    #     print number_of_columns
    #     print number_of_rows

    #     items = []
    #     rows = []

    #     for row in range(1, number_of_rows):
    #         values = []
    #         for col in range(number_of_columns):
    #             value  = (sheet.cell(row,col).value)
    #             # value = str(int(value))
    #             # values.append(value)
    #             try:
    #                 value = str(int(value))
    #             except ValueError:
    #                 pass
    #             finally:
    #                 values.append(value)
    #         print 'list of data',values



def task_read(request):
    print (">>>>>>>>>>>>>>>>>>>>>>>>>")

    if request.method == 'POST' and request.FILES['myuploadfile']:
        form = ExcelUploadForm(request.POST,request.FILES)
        myfile = request.FILES['myuploadfile']
        print (myfile)
        uploads = upload_files.objects.create(excel_files=myfile)
        print uploads
        message1 = 'file upload successfully'

        #================= another way  to create file  ==
        # uploads_one = upload_files(excel_files=myfile)
        # uploads_one.save()
        
        return render(request,'pcmaster.html',{'msg':message1})
    
    # return HttpResponse('pc master funtinality')
    return render(request,'pcmaster.html',{})
def shotdata(request):            
    shotsdata = Shots.objects.all()
    return render(request,'shottask.html',{'details':shotsdata})
def  shotsupervesior(request):
    print request.user,">>>>"    
    # Shots.objects.filter(supervisor='1669.0').update(supervisor=int('1669'))
    shotsdata = Shots.objects.filter(supervisor=request.user)
    artistdata=Shots.objects.filter(assigned="p6903")
    print artistdata,"LLLLLLLLL"
    assignedartist=UsersModel.objects.filter(user_role=2)
    print shotsdata
    # shotsdata = Shots.objects.filter(supervisor = 1669)
    print assignedartist,">>>>"
    return render(request,'my_shots.html',{'shotkey':shotsdata,'artists':assignedartist})

def update_shots(request):
    print "update shots view"
    if request.method == 'GET':
        art = request.GET.get('artist')
        print art
        sht_id = request.GET.get('shot_id')
        print sht_id
        # updata=Shots.objects.filter(assigned=sht_id=sht_id)
        updata = Shots.objects.filter(id=sht_id).update(assigned=art)
        print updata

        return HttpResponseRedirect('/process/shotsup/')
    else:
        pass
    return render(request,'my_shots.html',{'keys':updata})
def assignedshot(request):
    print request.user
    assign_dat=Shots.objects.filter(assigned=request.user)
    print assign_dat,"{{{{"
    return render(request,"artist_assignedshots.html",{'keys_data':assign_dat})