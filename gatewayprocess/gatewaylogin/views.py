from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import UsersModel,renderdata,episodes,subjectdetails,project,models,upload_files,Tasks,Shots,genticketing,assests,creteassestdata
from .forms import loginform,changeform,ticketlogform,ExcelUploadForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as signout 
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.conf import settings
from xlrd import open_workbook
import datetime
import os
import xml.etree.ElementTree as ET
from django.utils import timezone
import pytz
from django.views.decorators.csrf import csrf_exempt
#login functionality
def login(request):
    ''' Login '''
    error_message = ""
    print ("login view")
    if request.method == 'POST':
        form = loginform(request.POST)  
        print ('after post method')  
        print request.POST    
        password = request.POST.get('password')
        name = request.POST.get('Firstname')   
        print (name, password)     
        if form.is_valid():
            print ('form is valid')
            user = authenticate(username=name,password=password)        
            #print ("valid")                                     
            auth_login(request, user)
            # auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            #print name
            user_id = UsersModel.objects.filter(username=name)
            print (user_id),":::::::::::::::::::::::::"
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
    print request.user 
    get_Data = UsersModel.objects.get(id=1)
    print "get method"
    print get_Data
    print type(get_Data)
    print get_Data.email
    # get_Data1 = UsersModel.objects.filter(id=80)
    # print get_Data1

    user_id = UsersModel.objects.filter(username=request.user.username)
    # print user_id
    # print type(user_id)
    # print "***"
    # all_data = UsersModel.objects.all()
    # print all_data
    # print type(all_data)

    # for i in all_data:
    #     print i.username
    # print "***"

    # val = UsersModel.objects.values()
    # print val
    # print type(val)
    
    # for i in val:
    #     print i['username']
    

    return render(request, 'profile.html', {'data':user_id})
#setting the newuserand pwd
def create_new_user(request):
    # users = UsersModel.objects.create(username='1400',user_role=2,email="budda@gmail.com",
    #     first_name="sunitha")

    users = UsersModel.objects.get(username='p6852')

    users.set_password("gateway@123")


    users.save()
    # var = UsersModel.objects.all()
    # for i in var:
    #     data=UsersModel.objects.get(username=i.username)


    #     data.set_password("gateway@143")
    #     data.save()
    return HttpResponse('use created or updated')

@login_required(login_url='/process/log/')
# @login_required
#change password
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
            #request.user.username is loggineduser        
            user=UsersModel.objects.get(username=request.user.username)
            # u.set_password('new password')
            #set_password is to convert hashkeyformat 
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
#logout functionality
def logoutin(request):
    signout(request)
    return redirect('/process/log/')
@login_required(login_url='/process/log/')    
#tasking status 
def taskin(request):            
    tasks_data_all = Tasks.objects.all()
    #print "===="*20
    #print type(tasks_data_all)
    #print tasks_data_all
    #print "===="*20

    # for kk in user:
    #     print kk.created_at,"$$$$"
    layerdat=["char_matte","bg_matte","char_clr"]
    prioity=["high","medium","low"]
    renderinfo=["select","all_passes","few_passes"]
    # print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    list1 = ['STATUS','ACCEPTED','WIP', 'COMPLETE']
    # print("Task successfully created")
    list2 = ['ASSIGNED','p6852','p6851','p6857', 'p6855']
    # print("Task successfully created")
    #####################################
    userdata=UsersModel.objects.values()
    #print userdata,"{{{{{{{{{{{["
    #print "===="*20

    developers_list = []
    for each in userdata:
        #print each,"eeeeeeeeeeeee"
        if each["user_role"]==3:
            developers_list.append(each["username"])
    #print "**************"  
    #print developers_list
    ###################################

    if request.method == 'GET':

        #print "for dates gettinginfo"
        dateinfo1=request.GET.get('check_date1') 
        dateinfo2=request.GET.get('check_date2')
        
        #print dateinfo1,dateinfo2,">>>"
        # datetime_object = datetime.strptime('dateinfo1', '%M %d %Y')
        if dateinfo1 and dateinfo2:
            #print "s"
            dateinfo1=dateinfo1.split('-')
            dateinfo2=dateinfo2.split('-')
            #print dateinfo1[::-1]       
            dateinfo1 = [str(x)for x in dateinfo1]
            #print dateinfo1,"}}}}}}}]"
            dateinfo2 = [str(x)for x in dateinfo2]
            #print dateinfo2,">>>>>>>>>"
            st_date = datetime.date(int(dateinfo1[0]),int(dateinfo1[1]),int(dateinfo1[2]))
            #print st_date,"<<<<<<<<"
            st1_date=datetime.date(int(dateinfo2[0]),int(dateinfo2[1]),int(dateinfo2[2]))
            #print st1_date,"sssss"
            # data = Tasks.objects.filter(created_at__contains=st_date)
            # print data,"getttig data"

            # datainfo1=datainfo1, datainfo2=datainfo2
            # s_date=datetime.strptime(str(dateinfo1), '%m-%d-%Y %H:%M:%S.%f')

            ## below query is getting date range data
            ##_______________created_at__range=database lo column name#________#
            date_range_tasks=Tasks.objects.filter(created_at__range=(st_date, st1_date))

            #print date_range_tasks,"##################"
            
            # return JsonResponse

            # datetime_object = datetime.strptime('dateinfo1', '%b %d %Y %I:%M%p')
            # print date_range_tasks,">>>>>>"

            # server.query('tasks',filters=[['creaetd_at','in',[101,123]],['name','sunitha']])
            # server.query('tasks',filters=[[]])

            data_list = []
            # [[],[],[]]
            for i in date_range_tasks:
                r_list = []
                r_list.append(i.id)
                r_list.append(i.assigned)
                r_list.append(i.process)
                r_list.append(i.supervisor)
                r_list.append(i.status)
                r_list.append(i.created_at) 
                #print "&&&&" , i.created_at, "&&&&"
                r_list.append("Reallot")
                r_list.append("asset_data")
                r_list.append("render_layer")
                data_list.append(r_list)

            ''' generate table start '''

            head_list = ['Task No','Assigned','Process','Supervisor','Status','Time','reallot','asset_data', 'render_layer']        
            div_root = ET.Element('div')
            tab = ET.SubElement(div_root, 'table',id="taskTable", clas='table',border='1')
            thr_root = ET.SubElement(tab, 'tr')       
            
            for i in head_list:
                tad = ET.SubElement(thr_root,'td').text=str(i)

            #print "getting data",data_list
            for  j in data_list:
                # print j[0],"KKKKKKKKKKKKKKKKKKKKK"
                tr_root = ET.SubElement(tab, 'tr')                
                
                # j = [12,'p6907','namita, 'lighting','date', 'reallot', 'asset_data','render_layer']
                for k in j:
                    # print j[0],"iiiii"
                    print k

                    if k == "Reallot":
                        tad = ET.SubElement(tr_root,'td')
                        # ET.SubElement(tad,'button',onclick="sunitha()",id="%s"%(j[0]), clas='btn btn-danger').text='Rellot'                       
                        ET.SubElement(tad,'button',onclick="sunitha()",id="{0}".format(j[0]), clas='btn btn-danger').text='Rellot'                       

                    
                    elif k=="asset_data":
                        tad = ET.SubElement(tr_root,'td')
                        ET.SubElement(tad,'button',onclick="assestnamesunitha()",id="%s"%(j[0]),clas='btn btn-success').text='asset_data'
                    elif k=="render_layer":
                        # if k == "ligthing":
                        tad = ET.SubElement(tr_root,'td')
                        ET.SubElement(tad,'button',id="{0}".format(j[0]),type="button",clas='RenderBtn btn btn-primary suni').text='render_layer'
                        # else:
                        #     tad = ET.SubElement(tr_root,'td').text="-" 
    
                    else:
                        tad = ET.SubElement(tr_root,'td').text=str(k)     


            datewise_tasks_data = ET.tostring(div_root).replace('clas','class')
            #print datewise_tasks_data,"[[[[["
            # print popup_data

            data = {'task_info':datewise_tasks_data}
            # if data['is_taken']:
            #     data['error_message'] = 'A user with this username already exists.'
            return JsonResponse(data)

        


            ''' generate table end '''

        else:
            pass
        
        getval=request.GET.get('check_this')        
        iddata=request.GET.get('user_id')
        assdata=request.GET.get('assign_dat')
        # print (getval,iddata),("<<<<<<<<<<<<")
        #print (assdata)
        update_data = Tasks.objects.filter(login=iddata).update(status=getval,assigned=assdata)
        print('task data updated')


        # to_update = TestModel.objects.filter(id=2).update(name='updated_name', key=new_key)
    else:
        return render(request,'task.html',{'details':tasks_data_all,'status':list1,'assigned':list2,'keydevelopers':developers_list}) 

        
    return render(request,'task.html',{'details':tasks_data_all,'status':list1,'assigned':list2,'keydevelopers':developers_list,"layers":layerdat,"process":prioity,"data":renderinfo}) 
#======= reallotment task updation
def reallot_task_update(request):
    '''reallotment task updation'''

    print request.GET, "####"

    if request.method == "GET":
        #assign_id  this s from models.py#
        user = request.GET.get('assign_id')
        task_id = request.GET.get('task_id')
        print user,task_id, "^^^^^^^^^^^^^^^6"
        # user = "p6852"
        #username=database lo field name#
        nameinfo=UsersModel.objects.filter(username=user)
        # print nameinfo,"LLLL"
        name=""
        for i in nameinfo:
            # print i.first_name
            #first_name=database lo unna field name#
            name=i.first_name
        print name,user,task_id
        dateinfo=datetime.datetime.today().strftime('%Y-%m-%d')
        present_time = datetime.datetime.now()
        print ">>>>>>>>>>>>",present_time
        print dateinfo,"ddddd"
        # dateinfo=UsersModel.objects.filter(last_login=user)
        # for dat in dateinfo:
        #     date=dat.last_login,"JJJJJJJJJJJJJ"
        ### task update query
        update_task = Tasks.objects.filter(id=task_id).update(assigned=user,supervisor=name,created_at=present_time)
        # print update_task

        print "reallotment updated"
        success = {'msg':'reallotment updated'}
        return JsonResponse(success)

    pass

#===============

def gen_ticketing(request):            
    # user = genticketing.objects.all()s
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
        print request.GET
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
    return HttpResponse("tasks successfully inserted")



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
def shotsupervesior(request):
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

def reporting(request):
    episodes_list = []
    ep = episodes.objects.all()
    print ep,"||||||||||||||||||"
    episodes_dict = {}
    # print ep
    for i in ep:
        print i,"<<<<<<<<<<"
        ep_list = str(i.episodes).split(',')
        # print "&&&&&&&&&777",ep_list
        episodes_dict[str(i.project_name)]=ep_list
        
    print '>>>>>>>>>>>>>>',episodes_dict

    # print '^^',episodes_dict['five_it'][0]
    # basic_list = []
    project = 'five_it'
    if project == 'five_it':
        print "*************",episodes_dict[project]
        r_list = []       
    
        for each in episodes_dict[project]:
            print each,"LLLLLLLLL"
            var=Shots.objects.filter(projectname="five_it",episode=each)
            w=0
            c=0
            a=0
            assign_c=Shots.objects.filter(projectname="five_it",episode=each,status='assigned')
            wip_c=Shots.objects.filter(projectname="five_it",episode=each,status='WIP')
            comp_c=Shots.objects.filter(projectname="five_it",episode=each,status='complete')            
            basic_list = []

            basic_list.append(project)
            basic_list.append(each)            
            basic_list.append(len(assign_c))
            basic_list.append(len(wip_c))
            basic_list.append(len(comp_c))
            r_list.append(basic_list)
            # print "}}}}",each,basic_list
        print "$$$$$$$$$$$$$$$$$$$$$$$",r_list
        head_list = ['Project','Episode','assigned','wip','complete']
        
        div_root = ET.Element('div')
        tab = ET.SubElement(div_root, 'table', clas='table',border='1')
        thr_root = ET.SubElement(tab, 'tr')
        
        for i in head_list:
            tad = ET.SubElement(thr_root,'td').text=str(i)
        
        for no,j in enumerate(r_list):
            tr_root = ET.SubElement(tab, 'tr')
            for number,k in enumerate(j):
                # print ")))",k
                tad = ET.SubElement(tr_root,'td', id='{0}?{1}?{2}'.format(project,episodes_dict[project][no],head_list[number])).text=str(k)
            #break

 
        data = ET.tostring(div_root).replace('clas','class')

        return render(request,'reported.html',{'listdata':basic_list, 'table_data':data})


def reporting1(request):
    #episodes_list = []
    getdatafrommodel = Shots.objects.all()
    #print ep,"||||||||||||||||||"
    episodes_data=[]
    projects_data=[]
    statusdata=[]
    # print ep
    for i in getdatafrommodel:
        print i,"<<<<<<<<<<"
        episodes_data.append(i.episode)
        projects_data.append(i.projectname)
        statusdata.append(i.status)
    episodes_datadup=list(set(episodes_data)) 
    projects_data=list(set(projects_data))
    statusdataup=list(set(statusdata))
    print "===============",statusdataup
    print projects_data
    print episodes_datadup
    datadic={}
    for i in projects_data:
        addata=[]
        for j in episodes_datadup:
            totaldic={}
            totaldic[j]=statusdataup
            addata.append(totaldic)
        datadic[i]=addata
    print datadic,":::::::::::::::::::"
    finalapp=[]
    # for ep,sho in datadic.items():
    #     stadat=[]
    #     for each in sho:
    #         print each
    #         for j,k in sho.items():
    #             for each1 in k:
    #                 print each1,">>>>>>>>>>>"
    return None


        
def reporting_popup(request):
    ''' popup report generation'''

    if request.method == "GET":
        print "pop up view",request.GET.get('status_report')
        request_from_report_table = str(request.GET.get('status_report'))
        data11 = request_from_report_table.split('?')#five_it?100?wip

        print data11

        if data11[2] == 'wip':
            data11[2] = data11[2].upper()

        shots_data = Shots.objects.filter(projectname=data11[0],episode=data11[1],status=data11[2])

        print "shots data is ",shots_data
        data_list = []
        for i in shots_data:
            r_list = []
            r_list.append(i.projectname)
            r_list.append(i.episode)
            r_list.append(i.status)
            data_list.append(r_list)

        print "$$$$$$$$$$$4",data_list
        head_list = ['Project','Episode','status']        
        div_root = ET.Element('div')
        tab = ET.SubElement(div_root, 'table',id="popupTable", clas='table',border='1')
        thr_root = ET.SubElement(tab, 'tr')       
        
        for i in head_list:
            tad = ET.SubElement(thr_root,'td').text=str(i)

        for j in data_list:
            tr_root = ET.SubElement(tab, 'tr')
            for k in j:                
                tad = ET.SubElement(tr_root,'td').text=str(k)     


        popup_data = ET.tostring(div_root).replace('clas','class')

        print popup_data

        data1 = {'is_popupdata':popup_data}
        # if data['is_taken']:
        #     data['error_message'] = 'A user with this username already exists.'
        return JsonResponse(data1)

    return HttpResponse('popup')
def det(request):
    data=subject.objects.create(collegename="bsit",branch="eee",year="2016")
    return HttpResponse("data is inserted")

def filteringdata(request):
    yearslist=[]
    ye=subjectdetails.objects.all()
    yearsdict={}
    yelist = []
    for i in ye:
        print i.branch,":::::::"
        print i.year,"<<<<<<<<<<<<<<<"        
        
        yelist.append(i.year)
        yearsdict[str(i.collegename)]=list(set(yelist))
    print yearsdict,":::::::::::::::::"
    collegename="bsit"
    if collegename=="bsit":
        print "coming"
        newlist=[]
        for each in yearsdict[collegename]:
            print each,"}}}}}}}}}}}}}}"
            ece=0
            eee=0
            cse=0
            eeedetails=subjectdetails.objects.filter(collegename="bsit",year=each,branch="eee")
            ecedetails=subjectdetails.objects.filter(collegename="bsit",year=each,branch="ece")
            csedetails=subjectdetails.objects.filter(collegename="bsit",year=each,branch="cse")
            firstpartadd=[]
            firstpartadd.append(collegename)
            firstpartadd.append(each)
            # newlist.append(firstpartadd)
            # print newlist,"PPPPPPPPPPP"
            firstpartadd.append(len(ecedetails))
            firstpartadd.append(len(eeedetails))
            firstpartadd.append(len(csedetails))
            newlist.append(firstpartadd)
        print newlist,"{{{{{{"
        first_list = ['collegename','year','ece','eee','cse']
        div_root = ET.Element('div')
        tab = ET.SubElement(div_root, 'table', clas='table',border='1')
        thr_root = ET.SubElement(tab, 'tr')
        
        for i in first_list:
            tad = ET.SubElement(thr_root,'td').text=str(i)
        
        for j in newlist:
            # print j,"LLJJJJJ"

            tr_root = ET.SubElement(tab, 'tr')
            for number,k in enumerate(j):
                #print ")))",k
                tad = ET.SubElement(tr_root,'td', id='{0}?{1}?{2}'.format(collegename,yearsdict[collegename][0],first_list[number])).text=str(k)
            # break 
        data = ET.tostring(div_root).replace('clas','class')

    return render(request,'staticdata.html',{'listdata':firstpartadd, 'table_data':data})

def filteringdata_version2(request):
    get_all_records=subjectdetails.objects.all()
    college_names_list = []
    yearslist = []
    branchlist=[]    
    for i in get_all_records:
        #print i.branch,":::::::"
        # print i.year,"<<<<<<<<<<<<<<<"
        college_names_list.append(i.collegename)                
        yearslist.append(i.year)
        branchlist.append(i.branch)
    college_names_list = list(set(college_names_list))
    yearslist = list(set(yearslist))
    branchlist = list(set(branchlist)) 

    data_dict={}
    for i in college_names_list:
        adlist=[]
        for k in yearslist:
            lidic={}
            lidic[k]=branchlist
            adlist.append(lidic)
        #     print "inside dict",lidic
        # print "college",i
        # print ">>>>>>>>>",adlist
        data_dict[i]= adlist 
    # print data_dict,":::::::::::::::::"
    final_list = []
    for col,values_list in data_dict.items():
        # print col,"^^^^^^^^^",values_list,"<<<<<<<<<<<<<<<<"
        college_wise_list = []
        for year_dict in values_list:
            # print "&&&",year_dict

            for year,branches in year_dict.items():
                # print year, branches
                
                for branch in branches:
                    inside_data_list=[]
                    
                    eee_count=subjectdetails.objects.filter(collegename=col,year=year,branch=branch)
                    ece_count=subjectdetails.objects.filter(collegename=col,year=year,branch=branch)
                    cse_count=subjectdetails.objects.filter(collegename=col,year=year,branch=branch)
                    inside_data_list.append(col)
                    inside_data_list.append(year)
                    inside_data_list.append(len(eee_count))
                    inside_data_list.append(len(ece_count))
                    inside_data_list.append(len(cse_count))            
                college_wise_list.append(inside_data_list)
                    # print eee_count,ece_count,cse_count,"}}}}}}}}}}}}}}}"
        final_list.extend(college_wise_list)
    print final_list,"{{{{{{{{{{{{{{]]]]]]]]]]]]]]]]"

    first_list = ['collegename','year','ece','eee','cse']    
    data=tablecreationdata(request,head_list=first_list,first_list=final_list)
            

    return render(request,'static_data_version_2.html',{'table_data':data, 'colleges':list(set(college_names_list)), 'years':list(set(yearslist))})
    


def projectname(request):
    var=Shots.objects.filter(projectname="five_it",episode="100")
    w=0
    c=0
    a=0
    assign_c=Shots.objects.filter(projectname="five_it",episode="100",status='assigned')
    wip_c=Shots.objects.filter(projectname="five_it",episode="100",status='WIP')
    comp_c=Shots.objects.filter(projectname="five_it",episode="100",status='complete')
    r_list = []
    basic_list = []
    for j in var:
        basic_list.append(j.projectname)
        basic_list.append(j.episode)
        break
    basic_list.append(len(assign_c))
    basic_list.append(len(wip_c))
    basic_list.append(len(comp_c))
    r_list.append(basic_list)
    print "}}}}",basic_list
    print "^^^",r_list
    head_list = ['Project','Episode','assigned','wip','complete']
    ''''''
    div_root = ET.Element('div')
    tab = ET.SubElement(div_root, 'table', clas='table',border='1')
    thr_root = ET.SubElement(tab, 'tr')
    tr_root = ET.SubElement(tab, 'tr')
    for i in head_list:
        tad = ET.SubElement(thr_root,'td').text=str(i)
    
    for j in r_list:
        for k in j:
            tad = ET.SubElement(tr_root,'td', id='{0}'.format(k)).text=str(k)


    data = ET.tostring(div_root).replace('clas','class')

    return render(request,'reported.html',{'listdata':basic_list, 'table_data':data})
 
def staticdata(request):
    first_list = ['collegename','year','ece','eee','cse']
    second_list=['bsit','2007','50','30','49']
    div_root = ET.Element('div')
    tab = ET.SubElement(div_root, 'table', clas='table',border='1')
    thr_root = ET.SubElement(tab, 'tr')
    tr_root = ET.SubElement(tab, 'tr')
    for i in first_list:
        print i,"::::::::::::"
        tad = ET.SubElement(thr_root,'td').text=str(i)
    for j in second_list:
        print j,"}}}}}}}}}}}}"
        #tr_root = ET.SubElement(tab, 'tr')

        #for k in j:
            #print k,"::::::::::::::>>>>>"
        tad = ET.SubElement(tr_root,'td').text=str(j)


    getdata = ET.tostring(div_root).replace('clas','class')

    return render(request,'staticdatas.html',{'table_datas':getdata})


def create_projects_episodes(request):
    episodesdata = {
    'five_it' : ['100','101','102','103','121','125','123','125','127','130'],
    'jbs3': ['300','301','302','303','304','305','306','310']
    }

    for j,v in episodesdata.items():
        print j,v,":::::::::"
        dd = ",".join(v)
        print dd
        episodes.objects.create(project_name=j,episodes=dd)
    return HttpResponse('data inserted')
    # episodesdata = {
    # 'five_it' : ['100','101','102','103','121','125','123','125','127','130'],
    # 'jbs3': ['300','301','302','303','304','305','306','310']
    # }

    # for j,v in episodesdata.items():
    #     print j,v,":::::::::"
    #     episodes.objects.create(project_name=j,episodes=v)

    # # pass
def det_popup(request):
    if request.method == "GET":
        print "===============",request.GET.get('student_report')
        # bsit?2017?ece
        get_id = request.GET.get('student_report')
        list1 = get_id.split("?")

        print "???????????????",list1
        ss_data=subjectdetails.objects.filter(collegename=list1[0],year=list1[1],branch=list1[2])
        
        finalap=[]
        for each in ss_data:
            app=[]
            print each.collegename,">>>>>>>>>>>>>>>>"
            print each.year
            print each.branch
            app.append(each.collegename)
            app.append(each.year)
            app.append(each.branch)            
            finalap.append(app)
        print finalap
        headinglist=["collegename","year","branch"]


        div_root = ET.Element('div')
        tab = ET.SubElement(div_root, 'table', clas='table',border='1')
        thr_root = ET.SubElement(tab, 'tr')
        
        for i in headinglist:
            tad = ET.SubElement(thr_root,'td').text=str(i)
        
        for j in finalap:
            tr_root = ET.SubElement(tab, 'tr')
            print j
            for k in j:
                # print  "$$$$$$$$$$$$$$$$$4",k
                tad = ET.SubElement(tr_root,'td', id='{0}'.format(k)).text=str(k)
        data = ET.tostring(div_root).replace('clas','class')
        print "table datat ====",data
        data_dict = {'popup_data':data}
        return JsonResponse(data_dict)

def ajax_filter_data_studentdetails(request):
    ''' code for ajax request start '''

    if request.method == "GET":


        print ">>>>>>>>>>>>>",request.GET
        yearList=request.GET.getlist('sel_year[]')   
        collegeList = request.GET.getlist('sel_college[]')
        print collegeList,yearList,"LLLLLLLLLLLLL"

        # yearList = ['2015','2017']
        # collegeList = ['bsit','cbit']
        print "&&&&&",yearList,collegeList
        print  type(yearList)
        # s_data = subjectdetails.objects.filter(collegename='bsit',year='2015')
        s_data = subjectdetails.objects.filter(collegename__in=collegeList,year__in=yearList)

        final_list=data_calling(request,db_records=s_data)                
        first_list = ['collegename','year','ece','eee','cse']    

        data11=tablecreationdata(request,head_list=first_list,first_list=final_list)
        print data11,"ajax request table"
        response_data = {'filter_data':data11}

        return JsonResponse(response_data)
    #return render(request,)
    ''' code for ajax request end '''

def tablecreationdata(request, head_list=[],first_list=[],name="",list1=[]):    
    div_root = ET.Element('div') # <div>
    tab = ET.SubElement(div_root, 'table', clas='table',border='1') # <div><table>
    thr_root = ET.SubElement(tab, 'tr') # <div><table><tr>
    
    for i in head_list:
        tad = ET.SubElement(thr_root,'th').text=str(i) # <div><table><tr><th></th><th></th><th></th><th></th><th></th></tr>
    
    
    for index1,j in enumerate(first_list):  
        tr_root = ET.SubElement(tab, 'tr')  # <div><table><tr><th>5times</th></tr><tr>    
        for number,k in enumerate(j): 
            print k,"::::::::"
            
            # for no, value in enumerate(k):            
            tad = ET.SubElement(tr_root,'td', id='').text=str(k)   # <div><table><tr><th>5times</th></tr><tr><td>length of k times</td></tr></table></div>                                     

    data = ET.tostring(div_root).replace('clas','class')
    return data

def data_calling(request, db_records=[]):
    #get_all_records=subjectdetails.objects.all()
    college_names_list = []
    yearslist = []
    branchlist=[]    
    for i in db_records:
        #print i.branch,":::::::"
        # print i.year,"<<<<<<<<<<<<<<<"
        college_names_list.append(i.collegename)                
        yearslist.append(i.year)
        branchlist.append(i.branch)
    college_names_list = list(set(college_names_list))
    yearslist = list(set(yearslist))
    branchlist = list(set(branchlist)) 

    data_dict={}
    for i in college_names_list:
        adlist=[]
        for k in yearslist:
            lidic={}
            lidic[k]=branchlist
            adlist.append(lidic)
        #     print "inside dict",lidic
        # print "college",i
        # print ">>>>>>>>>",adlist
        data_dict[i]= adlist 
    # print data_dict,":::::::::::::::::"
    final_list = []
    for col,values_list in data_dict.items():
        # print col,"^^^^^^^^^",values_list,"<<<<<<<<<<<<<<<<"
        college_wise_list = []
        for year_dict in values_list:
            # print "&&&",year_dict

            for year,branches in year_dict.items():
                # print year, branches
                
                for branch in branches:
                    inside_data_list=[]
                    
                    eee_count=subjectdetails.objects.filter(collegename=col,year=year,branch=branch)
                    ece_count=subjectdetails.objects.filter(collegename=col,year=year,branch=branch)
                    cse_count=subjectdetails.objects.filter(collegename=col,year=year,branch=branch)
                    inside_data_list.append(col)
                    inside_data_list.append(year)
                    inside_data_list.append(len(eee_count))
                    inside_data_list.append(len(ece_count))
                    inside_data_list.append(len(cse_count))            
                college_wise_list.append(inside_data_list)
                    # print eee_count,ece_count,cse_count,"}}}}}}}}}}}}}}}"
        final_list.extend(college_wise_list)
    print final_list,">>>>>>>>>>"
    return final_list
def shotdetails(request):
    var=[]
    shots=Shots.objects.values()
    for each in shots:
        if each["projectname"]=='mrr':
            pass
            var.append(each)
    print var,"++++++++++"
    return HttpResponse(var)

def creationdata(request):   
    
    return render(request,'htmlpagecreation.html',{'sentdda':'data'})

def creationdata_display(request):
    import xml.etree.ElementTree as ET
    div_root=ET.Element('html')
    head=ET.SubElement(div_root,'head')
    title=ET.SubElement(head,'title').text="Testing"    
    div_body=ET.SubElement(div_root,'body')
    table_root1=ET.SubElement(div_body,'table',border="1",cls="table")
    headtitle=["Name","Gender"]
    # headdata=["Arjun","Tilotama","Anitha","sunitha","namitha","raviraj","kavitha"]
    names_list = [["Arjun",'M'],["Tilotama","F"],['Anitha','F'],['sunitha','F'],['namitha','F'],['raviraj','M'],['kavitha','F']]
    th_root=ET.SubElement(table_root1,'tr',)
    
    for i in headtitle:
        print i,"iiiiiiii"  
        td_root=ET.SubElement(th_root,'th').text=str(i)

    for j in names_list:
        tr_root=ET.SubElement(table_root1,'tr')
        for k in j:
            td_root=ET.SubElement(tr_root,'td').text=str(k)    

    table_data = ET.tostring(div_root).replace('cls','class')
    print table_data
    # with open('/home/sunitha/Desktop/data.html','w') as f:
    #     f.write(data)
    #     print data

    if request.method == "GET":
        data = {'success_data':table_data}
        return JsonResponse(data)
@csrf_exempt
def previewinfo(request):
    # seconddata=[]
    if request.method=="POST":
        print "&&&"*40
        print request.POST
        sheetinfo=request.POST.get('check_taskinfo')
        print sheetinfo,"KKKKKKKK"
        path = "/home/sunitha/Documents/practice_projects/data.xlsx"
        seconddata=excelreadinfo(path=path,sheetinfo=sheetinfo)        
        
        table_root1=ET.Element('table',border="1",cls="table")
        th_root=ET.SubElement(table_root1,'tr')
        for i in seconddata[0]:
            td_root=ET.SubElement(th_root,'th').text=str(i)
        
        for j in range(1,len(seconddata)):
            # j indicates index, seconddata[1]
            # tr_root1=ET.SubElement(table_root1,'tr').text=str(seconddata[j])
            tr_root1=ET.SubElement(table_root1,'tr')
            for val in seconddata[j]:
                ET.SubElement(tr_root1,'td').text=str(val)    
        table_data = ET.tostring(table_root1).replace('cls','class')
        data = {'lists':table_data}       
        
        return JsonResponse(data)


    return render(request,"pcmaster.html",{})
def assest_task(request):
    procesrel={'modeling':['96852','96851'],'rigging':['123','324'],'texturing':['1236','6788']}
    asset_type = ['chars', 'sets', 'props']
    if request.method=="GET":
        assestdata = request.GET.get('getinfo')
        texdat=request.GET.get('textre')
        print texdat, "LLLLLL"
        asset_names = {'chars':['tom','puppy'],'sets':['trainset'],'props':['set']}
        if assestdata:            
            print ">>>>",assestdata
            if assestdata in asset_names.keys():
                print asset_names[assestdata]
                asset_names_values = asset_names[assestdata]
                print asset_names_values

                select_root = ET.Element('select', id="exampleFormControlSelect3", clas="form-control")
                for charsinfo in asset_names_values:
                    ET.SubElement(select_root, 'option').text=charsinfo

                print ET.tostring(select_root)
                select_data =  ET.tostring(select_root).replace('clas','class')
                data = {'sss':select_data}
                return JsonResponse(data)

            else:
                print "check"
        elif texdat :
            procesrel={'modeling':['96852','96851'],'rigging':['123','324'],'texturing':['1236','6788']}
            print procesrel.keys() #['modeling','texturing']
            if texdat in procesrel.keys():
                supervisor_values = procesrel[texdat]
                print supervisor_values
                select_root = ET.Element('select', id="supervisorinfo", clas="form-control")
                for charsinfo in supervisor_values:
                    ET.SubElement(select_root, 'option').text=charsinfo

                print ET.tostring(select_root)
                select_data =  ET.tostring(select_root).replace('clas','class')
                data = {'sup':select_data}
                return JsonResponse(data)
            
        else:
            print "else"
    return render(request,'assestinfo.html',{"value":assestdata,'asset_types':asset_type})
#def Assestconcern(request):
    
#     path = "/home/sunitha/Documents/practice_projects/data.xlsx"
#     wb = open_workbook(path)
#     print ifwb
#     #print wb.sheet_by_name("assets")
#     tasks = wb.sheet_by_name("assets")        
#     print tasks
#     chars = []
#     props = []
#     sets = []
#     vehicles= []
#     for row in range(tasks.nrows):              
        
#         number_of_rows = tasks.nrows
#         number_of_columns = tasks.ncols        
#         for column in range(tasks.ncols):
#             # if tasks.cell(row,column).value == value:
#             print column,"LLLLLL"
#             print row, column
#             value  = (tasks.cell(row,column).value)
#             chars.append(tasks.cell(row,0).value)
#             props.append(tasks.cell(row,2).value)
#             sets.append(tasks.cell(row,1).value)
#             vehicles.append(tasks.cell(row,3).value)
#     charslist=list(set(chars))
#     charslist.remove('chars')
#     propslist=list(set(props))
#     propslist.remove('props')
#     setslist=list(set(sets))
#     setslist.remove('sets')
#     vehiclelist=list(set(vehicles))
#     vehiclelist.remove('vehicles')
#     ch = ",".join(charslist)
#     print ch
#     pr=",".join(propslist)
#     se=",".join(setslist)
#     vh=",".join(vehiclelist)
#     # insertdta=assests.objects.create(chars=ch,props=pr,sets=se,vehicles=vh)    
#     return HttpResponse(insertdta)
#@csrf_exempt
# def submitdata(request):
#     if request.method=='POST':
#         getselectboxval=request.POST.get('check_taskinfo')
#         print getselectboxval,"LLLL"
#         path= path = "/home/sunitha/Documents/practice_projects/data.xlsx"
#         iterexcel=excelreadinfo(path=path,sheetinfo=getselectboxval)
#         iterexcel.pop(0)
#         for li in iterexcel:
#             if getselectboxval=="create tasks":
#                 createindata=Tasks.objects.create(login=li[0],supervisor=li[1],status=li[2],assigned=li[3],process=li[4])
#             elif getselectboxval=="create shots":
#                 createindata=Shots.objects.create(shotno=li[0],episode=li[1],projectname=li[2],supervisor=li[3],assigned=li[4],process=li[5],status=li[6])
#             else:
#                 pass
#     return render(request,"pcmaster.html",{})
# def excelreadinfo(path="",sheetinfo=""):
#     seconddata=[]
#     wb = open_workbook(path)
#     sheetdet=wb.sheet_by_name(sheetinfo)
#     print sheetdet,":::::::::"
#     for row in range(sheetdet.nrows):              
#         dd = []
#         number_of_rows = sheetdet.nrows
#         number_of_columns = sheetdet.ncols        
#         for column in range(sheetdet.ncols):
#             print column,"hhhh"
#             value  = (sheetdet.cell(row,column).value)
#             #print value,"KKKKK"
#             # seconddata.append(value)
#             dd.append(value)

#         print list(set(dd))
#         seconddata.append(list(set(dd)))
#     print "KKKK",seconddata
#     return seconddata
# def asset_test(request):


#     asset_type = ['chars', 'sets', 'props']
#     asset_names = {'chars':['tom','puppy'],'sets':['trainset']}

#     process = ['modeling','rigging','texturing']

#     supervisors = {'modeling':['1550','1698']}
def submitdat(request):
    print "hello"
    if request.method=="GET":
        print request.GET, ">>>"
        data1 = request.GET.get('asset_type')
        print data1,"::::::"
        data2=request.GET.get('asset_name')
        data3=request.GET.get('asset_process')
        data4=request.GET.get('process_sup')
        descprition=request.GET.get('descpritioninfo')
        print "}}}}}", descprition
        finaldat=creteassestdata.objects.create(assesttypes=data1,nameofassests=data2,assestprocess=data3,processrelated=data4,descripition=descprition)
        data = {'message':'inserted'}
        return JsonResponse(data) 

    else:
        print "else"
def render_task(request):
    layerdat=["char_matte","bg_matte","char_clr"]
    prioity=["high","medium","low"]
    renderinfo=["select","all_passes","few_passes"]
    if request.method=="GET":   
        print request.GET
        keys_list = request.GET.keys()     
        for i in keys_list:
            print "&&&&",request.GET.getlist(i)
            dat = request.GET.getlist(i)
            print dat[0],dat[1],dat[2],dat[3],dat[4],dat[5],dat[6]
        
            insertdatabase=renderdata.objects.create(layer=dat[0],fromframe=dat[1],toframe=dat[2],totalframe=dat[3],prioirty=dat[4],renderdepth=dat[5],task_ids=dat[6])

    return render(request,'sendinglayers.html',{"layers":layerdat,"process":prioity,"data":renderinfo})
