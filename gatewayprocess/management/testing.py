# one = {
#     "Z:/sunitha/rig/sunitha.ma":["sunitha","sasank","swamy","swain"],    
#     "Z:/sunitha/rig/suneetha.ma":["sunitha","swain"],
    
# }

# two = {
#     "Z:/sunitha/lit/sunitha.ma":["sunitha","sasank","swamy"],
#     "Z:/sunitha/lit/suneetha.ma":["suneetha","data","sasank"]
# }
# print one.keys()
# print two.keys()

# for i in one.keys():
#     d=i.split('/')[-1]
#     for j in two.keys():
#         if j.__contains__(d):
#             print i,'-----YES ------', j
#             # print ">>>>",i
#             # print ">>>>>", j
#             # print two[j]
#             # print one[i]
#             for val in one[i]:
#                 if val in two[j]:
#                     print i,val, "YES"
#                 else:
#                     print i,val, "NO"
#         else:
#             print i,'----- NO ------', j
# one = {
#     "Z:/sunitha/rig/sunitha.ma":["sunitha","sasank","swamy","swain"]

# }
# two = {
#     "Z:/sunitha/lit/sunitha.ma":["sunitha","sasank","swamy"]
# }
# for i,j in one.iteritems():
#     for k  in two.keys()[0]:
#         if not k in j:
#             pass
# for i,j in one.iteritems():

#     for key, value in two.iteritems():

#         for  ii in j:
#             if ii in value:
#                 print ii, "YES", i
        # if i == key:
        #     print j,value

# import os
# src="/home/sunitha/274M-152"
# #sc=filter(lambda x:x.endswith(".ma"),os.listdir(src))
# print sc,"::::::"]
# d={"name":"sunitha","sub":[20,30,40,35],"dep":"eee"}
# d1=d["sub"]
# new=map(lambda x:x ,d1)
# print new,"mappppppp"
# new=filter(lambda x:x%2==0 ,d1)

# new_result = sum(map(lambda i:i, list(filter(lambda x:x%2==0 ,d['sub']))))
# print new_result , ">>>>>>>>>>"
# # Its giving an error
# new_result= [sum(int(i) for i in list(filter(lambda x:x%2==0 ,d['sub'])) )]

# print new_result,"&&&"
# l=[1,2,3]
# l2=[3,4,5]
# print zip(l,l2)
# result = [sum(i)  for i in zip(l,l2)]  
# print result
# ll =l + l2
# l3=[]
# for i in l:
#     for j in l2:
#         l3.append(i+j)
# print l3
# (1,6)

# input
# 0
# 1
# 2
# 3
# 4
# 5

# # output
# 0
# 1
# 0+1=1
# 1+1=2
# 1+2=3
# 2+3=5
# 3+5=8
# 5+8=13
# n=raw_input("enter the num")
# c=0
# first=0
# second=1
# for i in range(6):
    # inc=i
    # c=inc+i
    # inc=c
    # c=i
#     c=first+second
#     first=second
#     second=i
#     i+=1

#     # print first
    

# while c<=range(6):
#     print first
#     last=first+second
#     first=second
#     second=last
#     c+=1
# def prime_num(n):
#     # n=raw_input("Enter the number")
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print "prime",i
#                 break
#             # else:
#             #     print "not prime",i

# # prime_num(10)
# num=10
# if num > 1:  
#     for i in range(2,num):  
#         if (num % i) == 0:  
#             print(num,"is not a prime number")  
#             print(i,"times",num//,"is",num)  
#             break  
#         else:  
#             print(num,"is a prime number")  
         
# else:  
#    print(num,"is not a prime number")  

# def fibnocicc(n):
#     first=0
#     second=1
#     print first
#     print second
#     for i in range(0,n):
#         temp=first
#         first=second
#         second=temp+second
#         print second,"{{{{{"
# fibnocicc(6)
# def strpalinrome(st):
#     # st=raw_input("enter the string:")
#     new=st[::-1]
#     print new,"?????????"
#     if new == st:
#         print "palindrome"
#     else:
#         print "not palindrome"
# strpalinrome("laam")
# strpalinrome("malayalam")
# 
# def palindrome(n):
#     num=n
#     print ">>>"
#     d=0
#     rev=0
#     while num>0:
#         d=n%10
#         n=n/10
#         rev=rev*10+d
#     if (num==rev):
#         print "palindrome"
#         return True

#     else:
#         print "not palindrome"
#         return False
        

# # x=int(raw_input("enter the num:"))
# x=121
# palindrome(121)
# # if palindrome(x):
#     print ("palindrome")
# else:

#     print ( "not palindrome")



# palidrome()
# def amstrong():
#     for i in range(151):
#         n=i
#         result=0
#         n=str(len(i))
#         while(n!=0):
#             d=i%10
#             result=result+d**n
#             new=i//10
#             print new,"nn"
# amstrong()

# def righttriangle(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print ("**",end ="")
#         print ">>>>>>>>>>>>>"
# righttriangle(5)
# def numtriangle(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print (j,end="")
#         print ()
# numtriangle(6)
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))

# import sys

# list1 = [1,2,3]
# print sys.getsizeof(list1)
# tup = (1,2,3)
# print sys.getsizeof(tup)


# print list1.__sizeof__
# print tup__sizeof__

#method  overriding
# class A():
#     def data():
#         print "hi"


# class B(A):
#     def data():
#         print "hello"



# class A():
#     def data():
#         print "hi"


class B():
    def data():
        print "hello"

class C(B):
    def data():
        print ":::::::::::::"

a=C()
a.data()
print a