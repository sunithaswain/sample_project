# import xlrd
# import os
# srcpath="F:/sunita _jango/django_practice/django_sample_projects/gatewayprocess.xls"
# obj=xlrd.open_workbook(srcpath)
# sobj=obj.sheet_by_index(0)
# nc=sobj.nrows()
# nr=sobj.ncols()
# print nr,"??????????"
# for i in range(0,sobj.nrows):
#     print i





# import xlrd,os
# class Replacing:
#     def ExcelData(self,*args):
#         #path=raw_input("enter the path")
#         src = raw_input("enter the excel path (include the file name also): ").replace("\\","/")
#         if os.path.exists(src):
#             obj = xlrd.open_workbook(src)
#             dic = {}
#             sobj = obj.sheet_by_index(0)
#             nc=sobj.ncols
#             nr=sobj.nrows
#             fReplaceStr=""
#             for cr in range(1,nr):
#                 #print cr
#                 searchpath = sobj.cell_value(cr,0)
#                 replacepath = sobj.cell_value(cr,1)
#                 #print searchpath,"LLLLLLLLLLLLLLL"
#                 #print replacepath,"JJJJJJJJJJJJJJJJJJJJJJJ"
#                 dic[searchpath]=replacepath
#             self.filesdata(dic)
#         else:
#             print ("Search String not found in "+src)
#     def filesdata(self,dic,*args):
#         allPaths=[]
#         src_path = raw_input("enter the sourcepath:")
#         for root, dirs, files in os.walk(src_path):
#             for fil in files:
#                 fullpath = root + "/" + fil
#                 fullpath = fullpath.replace("\\", "/")
#                 if os.path.exists(fullpath):
#                     if fullpath.endswith(".ma"):
#                         fid = open(fullpath, "r")
#                         line = fid.read()
#                         fid.close()
#                         for key in dic.keys():
#                             key=str(key)
#                             #print key,"KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
#                             print dic[key]
#                             if key in line:
#                                 line=line.replace(key,dic[key])
#                                 #line = allPaths.append(line)
#                         fid=open(fullpath,"w")
#                         fid.write(line)
#                         fid.close()

# Replacing().ExcelData()
# raw_input("enter to Quit")
# a={'p6888':[10,23,5],'p6872':[5,5,6]}
# uprod={}
# for u,p in a.items():
#     for ip in p:
#         print ip,":;;;;;;;;;;"
#         try:
#             uprod[u]+= ip
#         except:
#             uprod[u] = ip

# print uprod
# z=[12,2,3]
# z1=[3,4,5]
# newdat=zip(z,z1)
# print newdat,"KKKKK"
# listdat=[x for x in sorted(newdat)]
# print listdat,"jjjj"
###in a string#################
# def palindrome():
#     dat="malyalam"
#     newdat=dat[::-1]
#     print newdat,"LLL"
#     if len(dat)==len(newdat):
#         print "yes palindome"
#     else:
#         print "no padlindome"
# palindrome()
#######in a number######
def palnum():
    dat=[121]
    newdat=dat[::-1]
    print newdat,"::::"
    if len(dat)==len(newdat):
        print "s"
    else:
        print "n"
        
palnum()


class A():
    def __init__(self, name="", value=None):
        pass
    def b(self,*args):
        print 's'

a = A()


a = A(name="sunitha", value="10")
b = A(name="anitha", value="20")
c = A(name="namitha", value="30")

# immutable objects can be used as keys in dict


try:
    a =  1/0

    print a
except ZeroDivisionError,IOError:
# except:
    print "error"

dict1 = {}

dict1['p6852']='suni'
dict1.update({'p6852':'sunitha'})
dict1.update({'p6851':'sunitha'})
dict1.update({'p6852':'sunitha'})

print dict1

