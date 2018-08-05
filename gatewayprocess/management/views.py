# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Table_schedule,Schedule
from django.shortcuts import render
from django.http import JsonResponse
import datetime
import xml.etree.ElementTree as ET

# Create your views here.
##in create_schedule at a time in database it vl create for scheduleview and table scheduleview
def create_schedule(request):
    projectdata=["mrr","fiveit","pdt","dms"]
    episde=["100","102","122","134"]
    dic={"asset":["modeling","texturing","rigging","asset_hair","matte_painting","fur"],
    "post":["lighting","fx","comp","mg"],
    "production":["layout","blocking","secondary","lipsync"]}
    if request.method == "GET":
        dat=request.GET.get("startdata")
        enddat=request.GET.get("enddata")
        prodat=request.GET.get("proinfo")
        epdat=request.GET.get("epde")       
        print dat,enddat,prodat,epdat
        print request.GET

        if enddat!=None and dat!=None and prodat!=None and epdat!=None:                 
            if enddat and dat:
                startdates=dat.split("-")
                print startdates,"{{{{{{{{{"
                enddates=enddat.split("-")
                datestart = [str(x)for x in startdates]
                dateend=[str(x)for x in enddates]
                print datestart,startdates,"::::"
                st_date = datetime.date(int(datestart[0]),int(datestart[1]),int(datestart[2]))
                st1_date=datetime.date(int(dateend[0]),int(dateend[1]),int(dateend[2]))
                # sss = datetime.datetime.strftime(st_date)
                # print ">>>", sss
                print st_date, "---", st1_date
                total_days = st1_date - st_date+datetime.timedelta(days=1)
                total_days =total_days.days
                print total_days
                dividingday=int(total_days)/3
                print dividingday,"lllll"
                # ====== Dates Separation for Asset =====
                assetstartdate=st_date
                assetenddate=st_date + datetime.timedelta(days=dividingday-1)
                print assetstartdate
                print assetenddate
                # ====== Dates Separation for Production =====
                productionstartdate=assetstartdate+datetime.timedelta(days=dividingday)
                # print prod
                productionenddate=assetenddate+datetime.timedelta(days=dividingday)
                print productionenddate,"6666"
                # ====== Dates Separation for Post =====
                poststartdate=productionstartdate+datetime.timedelta(days=dividingday)
                # print post,"pppp"
                postenddate=productionenddate+datetime.timedelta(days=dividingday)
                # print addforpost,":::::::::"
                c_schedule = Schedule.objects.create(startdate=st_date,enddate=st1_date,projectcode=prodat,episode=epdat,lock='NO')
                c_schedule.save()
                print ",,,,,,,,,,,", c_schedule
                sch_id = str(c_schedule.id)
                # print c_schedule.id, "&&&"
                # print type(c_schedule.id)
                print "dictionary"
                batch_list=[]
                for key,value in dic.items():
                    # print key, dic[key]
                    # for i in dic[key]:
                    #   print key, i            
                    for j in value:
                        # print key,j,"jjjj"
                        # Table_schedule.objects.create("startdate":dat,"enddate":enddat,"project":prodat,"episode":epdat,"process":j,"product_type":key)
                        if key=="asset":
                            print key,"kkk"

                            batch_list.append(Table_schedule(startdate=assetstartdate,enddate=assetenddate,project=prodat,episode=epdat,process=j,product_type=key,lock='NO',schedule_id=sch_id))
                        elif key=="production":
                            batch_list.append(Table_schedule(startdate=productionstartdate,enddate=productionenddate,project=prodat,episode=epdat,process=j,product_type=key,lock='NO',schedule_id=sch_id))
                        elif key=="post":
                            batch_list.append(Table_schedule(startdate=poststartdate,enddate=postenddate,project=prodat,episode=epdat,process=j,product_type=key,lock='NO',schedule_id=sch_id))

                # print ">>>",len(batch_list)
                Table_schedule.objects.bulk_create(batch_list)
                data = {'message':"Schedule successfully created"}
                return JsonResponse(data)
        else:
            print "not excute"

    else:
        return render(request,'management/createschedule.html',{'pro':projectdata,'ep':episde})
    return render(request,'management/createschedule.html',{'pro':projectdata,'ep':episde})
def tableschedule(request):
    schduleinfo=Schedule.objects.all()
    tbleinfo=Table_schedule.objects.all()
    return render (request,'management/table_creationforscheduler.html',{"scheuledata":schduleinfo,"tble":tbleinfo})
def filterdata(request):
    sch=Schedule.objects.all()
    print sch,"sss"
    prodata=[]
    epdata=[]
    product_type_list=['asset','post', 'production']
    for i in sch:
        print type(i),"}}}}}}"
        #print i.get(episode),">>>>>>>"
        # {"su":"ppo"}
        prodata.append(i.projectcode)
        epdata.append(i.episode)
        # print i.keys()
    #print prodata,epdata,"::::"
    return render(request,'management/selectedoptions_displaying.html',{"projectin":prodata,"ep":epdata,"product":product_type_list})

def ajax_filterdata(request):
    if request.method == "GET":
        profuldata=request.GET.get("projdat")
        epsde=request.GET.get("epsdedata")
        pro=request.GET.get("prdodata")
        print profuldata,epsde,pro,"}}}}}}}}}}}"
        table = Table_schedule.objects.filter(project=profuldata,episode=epsde,product_type=pro)
        print "^^^"
        if table:
            listdata=[]
            for i in table:
                print (i)
                datalist=[]
                datalist.append(i.startdate)
                datalist.append(i.enddate)
                datalist.append(i.project)
                datalist.append(i.process)
                datalist.append(i.product_type)
                datalist.append(i.episode)
                listdata.append(datalist)
                print listdata,"{{{{"

            # [[],[],[]]
            head_list = ['Start  Date','End Date','Project','Process','Product Type','Episode']        
            div_root = ET.Element('div')
            tab = ET.SubElement(div_root, 'table',id="taskTable", clas='table',border='1')
            thr_root = ET.SubElement(tab, 'tr')                   
            for i in head_list:
                tad = ET.SubElement(thr_root,'td').text=str(i)
            #print "getting data",data_list
            for  j in listdata:
                # print j[0],"KKKKKKKKKKKKKKKKKKKKK"
                tr_root = ET.SubElement(tab, 'tr')                       
                # j = [12,'p6907','namita, 'lighting','date', 'reallot', 'asset_data','render_layer']
                for k in j:
                    # print j[0],"iiiii"
                    # print k,"::::::::"
                    tad = ET.SubElement(tr_root,'td').text=str(k)     
            tasks_data = ET.tostring(div_root).replace('clas','class')
            print tasks_data
            data = {'task_info':tasks_data,"message":"Done"}
            return JsonResponse(data)

        else:
            data = {'task_info':"","message":"Not done"}        
            return JsonResponse(data)

def dropdowndata(request):
    sch=Schedule.objects.all()
    print sch,"sss"
    prodata=[]
    epdata=[]
    product_type_list=['product_type_view','schedule_view', 'process_view']
    for i in sch:
        print i,"}}}}}}"
        prodata.append(i.projectcode)
        epdata.append(i.episode)
        # print i.keys()
    print prodata,epdata,"::::"

    return render(request,'management/select_dropdown.html',{"projectin":prodata,"ep":epdata,"product":product_type_list})
def ajaxdata(request):
    print "ajax method"
    dataapp=[]
    if request.method=="GET":
        projdat=request.GET.get("projdat")
        epinfo=request.GET.get("epsdedata")
        proinfo=request.GET.get("prdodata") 
        print projdat,epinfo,proinfo,"::"
        if proinfo=="schedule_view":
            sch_data = Schedule.objects.filter(projectcode=projdat,episode=epinfo)
            for i in sch_data:
                listapp=[]
                listapp.append("checkbox")
                listapp.append(i.startdate)
                listapp.append(i.enddate)
                listapp.append(i.projectcode)
                listapp.append(i.episode)
                dataapp.append(listapp)
            head_list = ['checkbox','Start  Date','End Date','Project','episode']        
            div_root = ET.Element('div')
            tab = ET.SubElement(div_root, 'table',id="taskTable", clas='table',border='1')
            thr_root = ET.SubElement(tab, 'tr')                   
            for i in head_list:
                tad = ET.SubElement(thr_root,'td').text=str(i)
            #print "getting data",data_list
            for  no,j in enumerate(dataapp):
                # print j[0],"KKKKKKKKKKKKKKKKKKKKK"
                tr_root = ET.SubElement(tab, 'tr')                       
                # j = [12,'p6907','namita, 'lighting','date', 'reallot', 'asset_data','render_layer']
                for k in j:
                    if k=="checkbox":
                        tad = ET.SubElement(tr_root,'td')
                        ET.SubElement(tad,'input',type='checkbox',name='checkboxdata', id='checkid_{0}'.format(no))
                    else:
                        tad = ET.SubElement(tr_root,'td').text=str(k)     
            tasks_data = ET.tostring(div_root).replace('clas','class')
            print tasks_data
            data = {'task_info':tasks_data,"message":"Done"}
            return JsonResponse(data)

        # else:
        #     data = {'task_info':"","message":"Not done"}        
        #     return JsonResponse(data)


            # print type(sch_data)
        else:
            tab_data = Table_schedule.objects.filter(project=projdat,episode=epinfo)
            print tab_data,"gggg"
            firstdata=[]
            for i in tab_data:
                secondata=[]
                secondata.append("checkbox")
                # secondata.append("checkbox")
                secondata.append(i.startdate)
                secondata.append(i.enddate)
                secondata.append(i.project)
                secondata.append(i.episode)
                secondata.append(i.process)
                secondata.append(i.product_type)
                firstdata.append(secondata)
            head_list = ["checkbox",'Start  Date','End Date','Projectcode','Episode','process','producttype']        
            div_root = ET.Element('div')
            tab = ET.SubElement(div_root, 'table',id="taskTable", clas='table',border='1')
            thr_root = ET.SubElement(tab, 'tr')                   
            for i in head_list:
                tad = ET.SubElement(thr_root,'td').text=str(i)
            #print "getting data",data_list
            for val,j in enumerate(firstdata):
                # print j[0],"KKKKKKKKKKKKKKKKKKKKK"
                tr_root = ET.SubElement(tab, 'tr')                       
                # j = [12,'p6907','namita, 'lighting','date', 'reallot', 'asset_data','render_layer']
                for k in j:
                    if k=="checkbox":
                #         print k,"iiiii"
                #     # print k,"::::::::"
                        tad = ET.SubElement(tr_root,'td')
                        ET.SubElement(tad,'input',type='checkbox',name='checkboxdata', id='checkid_{0}'.format(val))     
                    else:
                        tad = ET.SubElement(tr_root,'td').text=str(k) 
            final_data = ET.tostring(div_root).replace('clas','class')
            print final_data
            data = {'task_info':final_data,"message":"Done"}
            return JsonResponse(data)

        # else:
        #     data = {'task_info':"","message":"Not done"}        
        #     return JsonResponse(data)
    else:
        print "else method"
    # print "hi"
    # data={}
    # return JsonResponse(data)
    #return render (request,select_dropdown.html,{})


def detailed_time_schedule(request):
    sch=Schedule.objects.all()
    print sch,"sss"
    prodata=[]
    epdata=[]
    product_type_list=['product_type_view','schedule_view', 'process_view']
    for i in sch:
        print i,"}}}}}}"
        prodata.append(i.projectcode)
        epdata.append(i.episode)
    prodata=set(prodata)
    epdata=set(epdata)
        # print i.keys()
    # print prodata,epdata,"::::"

    return render(request,'management/time_schedule.html',{"projectin":prodata,"ep":epdata,"product":product_type_list})


def ajax_time_schedule(request):
    dataapp=[]
    startvalue=[]
    endvalue=[]
    if request.method=="GET":
        projdat=request.GET.get("projdat")
        epinfo=request.GET.get("epsdedata")
        proinfo=request.GET.get("prdodata") 
        # print projdat,epinfo,proinfo,"::"
        if proinfo=="schedule_view":
            sch_data = Schedule.objects.filter(projectcode=projdat,episode=epinfo)
            if sch_data:
                d=None
                d1=None
                delta=None
                for stdata in sch_data:
                    startget=stdata.startdate
                    endget=stdata.enddate
                    print startget,endget,"ggg"
                    # print startget.date()
                    d=startget.date()
                    print d,"ddddd"
                    d1=endget.date()
                    print d1,"eeee"
                    delta=d1-d 
                    # if delta is not None:
                        # print delta,"}}}}}}}}]"
                    # for i in range(delta.days + 1):
                    #     print(d1 + datetime.timedelta(i))

                head_list = ['checkbox']
                # if delta is not None:
                for i in range(delta.days + 1):
                    splityear=str(d1 + datetime.timedelta(i)).split("-")
                    date_month =  splityear[1]+"-"+splityear[2]
                    # head_list.append(d1 + datetime.timedelta(i))
                    head_list.append(date_month)
                    print date_month, "^^^^"
                    # splityear=str(d1 + datetime.timedelta(i)).split("-")
                    
                    print(d1 + datetime.timedelta(i)), "$$$$$$"
                # head_list1=head_list
                # head_list1.remove("checkbox")
                for i in sch_data:
                    listapp=[]
                    #listapp.append("checkbox")
                    for ii in head_list:                   
                        listapp.append(ii)
                    dataapp.append(listapp)
                    print dataapp,"LLLLLL"
                    print i,">>>>>>>>>>."
                div_root = ET.Element('div')
                tab = ET.SubElement(div_root, 'table',id="taskTable", clas='table',border='1')
                thr_root = ET.SubElement(tab, 'tr')                   
                for i in head_list:
                    tad = ET.SubElement(thr_root,'td').text=str(i)
                #print "getting data",data_list
                for  no,j in enumerate(dataapp):
                    # print j[0],"KKKKKKKKKKKKKKKKKKKKK"
                    tr_root = ET.SubElement(tab, 'tr')                       
                    # j = [12,'p6907','namita, 'lighting','date', 'reallot', 'asset_data','render_layer']
                    for k in j:
                        tad = ET.SubElement(tr_root,'td')
                        if k=="checkbox":                            
                            ET.SubElement(tad,'input',type='checkbox',name='checkboxdata', id='checkid_{0}'.format(no)).text="Planned"
                        else:
                            print k, "-----------"
                            ET.SubElement(tad, 'input',type='hidden').text="@@@SS"

                tasks_data = ET.tostring(div_root).replace('clas','class')
                print tasks_data
                data1 = {'task_info':tasks_data,"message":"Done"}
                return JsonResponse(data1)
            else:
                data1 = {'task_info':"Data not available"}
                return JsonResponse(data1)
        elif proinfo == "product_type_view":
            
            producttype_schedule=Schedule.objects.filter(projectcode=projdat,episode=epinfo)
            print producttype_schedule
            print len(producttype_schedule), "&&&&"

            if producttype_schedule:
                d=None
                d1=None
                delta=None
                sch_id = []
                for stdata in producttype_schedule:
                    startget=stdata.startdate
                    endget=stdata.enddate
                    sch_id.append(stdata.id)
                    # print startget,endget,"ggg"
                    # print startget.date()
                    d=startget.date()
                    # print d,"ddddd"
                    d1=endget.date()
                    # print d1,"eeee"
                    delta=d1-d 
                    # if delta is not None:
                        # print delta,"}}}}}}}}]"
                    # for i in range(delta.days + 1):
                    #     print(d1 + datetime.timedelta(i))
                print sch_id, "^^^^"
                if len(sch_id) > 0:
                    sch_id = sch_id[0]
                producttype=Table_schedule.objects.filter(project=projdat,episode=epinfo, schedule_id = sch_id)
                print producttype
                print len(producttype), "&&&&"

                head_list = ['checkbox']
                # if delta is not None:
                for i in range(delta.days + 1):
                    splityear=str(d1 + datetime.timedelta(i)).split("-")
                    date_month =  splityear[1]+"-"+splityear[2]
                    # head_list.append(d1 + datetime.timedelta(i))
                    head_list.append(date_month)
                    # print date_month, "^^^^"
                    # splityear=str(d1 + datetime.timedelta(i)).split("-")
                    
                    # print(d1 + datetime.timedelta(i)), "$$$$$$"
                # head_list1=head_list
                # head_list1.remove("checkbox")
                for i in producttype:
                    listapp=[]
                    #listapp.append("checkbox")
                    for ii in head_list:                   
                        listapp.append(ii)
                        # print i, "##"
                        # print i.product_type
                        # print i.startdate
                        # print  ii, "$$"
                        # listapp.append(i.product_type)
                    dataapp.append(listapp)
                    # print dataapp,"LLLLLL"
                    # print i,">>>>>>>>>>."
                # for 
                div_root = ET.Element('div')
                tab = ET.SubElement(div_root, 'table',id="taskTable", clas='table',border='1')
                thr_root = ET.SubElement(tab, 'tr')                   
                for i in head_list:
                    tad = ET.SubElement(thr_root,'td').text=str(i)
                #print "getting data",data_list
                for  no,j in enumerate(dataapp):
                    # print j[0],"KKKKKKKKKKKKKKKKKKKKK"
                    tr_root = ET.SubElement(tab, 'tr')                       
                    # j = [12,'p6907','namita, 'lighting','date', 'reallot', 'asset_data','render_layer']
                    for k in j:
                        tad = ET.SubElement(tr_root,'td')
                        if k=="checkbox":                            
                            ET.SubElement(tad,'input',type='checkbox',name='checkboxdata', id='checkid_{0}'.format(no)).text="Planned"
                        else:
                            # print k, "-----------"
                            ET.SubElement(tad, 'input',type='hidden').text=str(k)

                tasks_data = ET.tostring(div_root).replace('clas','class')
                # print tasks_data
                data1 = {'task_info':tasks_data,"message":"Done"}
                return JsonResponse(data1)
            else:
                data1 = {'task_info':"Data not available"}
                return JsonResponse(data1)
            #msg={'task_info':'hii'}
            # return JsonResponse(msg)
        elif proinfo=="process_view":
            popinfo={'task_info':"hello"}
            return JsonResponse(popinfo)
def graph_data(request):
    return render (request,"management/graph_data.html")

        