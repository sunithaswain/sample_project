from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import UsersModel,episodes,subjectdetails,project,models,upload_files,Tasks,Shots,genticketing
from .forms import loginform,changeform,ticketlogform,ExcelUploadForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as signout 
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.conf import settings
from xlrd import open_workbook
import os
import xml.etree.ElementTree as ET
#login functionality
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
#setting the newuserand pwd
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

    return render(request,'staticdatas.html',{'listdata':firstpartadd, 'table_data':data})




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
        print request.GET.get('sel_year')
        print request.GET.get('sel_college')
        s_data = subjectdetails.objects.filter(collegename=str(request.GET.get('sel_college')),year=str(request.GET.get('sel_year')))

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

