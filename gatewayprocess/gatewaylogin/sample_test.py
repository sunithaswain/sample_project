# from django.db import models
# from gatewaylogin.models import subjectdetails
# print "hi"
# dc = {'bsit':{'year':['ece','eee','cse']}}

# dd = [
# 	{'bsit':{'2017':{'ece':1,'eee':3,'cse':4},
# 			'2016':{'ece':1,'eee':3,'cse':4}
# 			}
# 	}
# ]



# [
# [[u'cbit', u'2015', 0, 1, 0], [u'cbit', u'2017', 0, 0, 1], [u'cbit', u'2016', 0, 0, 1]], 
# [[u'bsit', u'2017', 1, 1, 0], [u'bsit', u'2016', 0, 3, 0]], 
# [[u'jntu', u'2015', 0, 0, 0], [u'jntu', u'2017', 0, 1, 0], [u'jntu', u'2016', 1, 1, 1]]
# ]

# [[u'cbit', u'2015', 0, 1, 0]]
# 	[[[u'cbit', u'2015', 0, 1, 0]]]

# [[[]]]





colege_name =['bsit','cbit']
years_list = [2016,2017]
branch_list = ['eee','ece']
d={}
for i in colege_name:
	dd=[]
	for k in years_list:
		jj = {}
		jj[k]=branch_list # inside dictionary

		dd.append(jj) # dictionaries list
		# dd[j]=branch_list
	d[i] = dd # collegename , list of dictionaries

{'cbit':[2016,2017],'bsit':[2016,2017]}

{'cbit':[{year,branches},{}]}


{'cbit': [{2016: ['eee', 'ece']}, {2017: ['eee', 'ece']}]}

print "dynamic",d
for i , j in d.items():
	print i,">>>>>>>>>>>>>>>>>",j
	for ii in j:
		for each, val in ii.items():
			print each , "*********", val
# dddd = {'bsit':[{'2015':['eee','ece']},{'2017':['eee','ece']}]}

# {'cbit': [{2016: ['eee', 'ece']}, {2017: ['eee', 'ece']}]}
# data = {'cbit': [u'2015', u'2017', u'2016'], 'bsit': [u'2017', u'2016'], 'jntu': [u'2015', u'2017', u'2016']} 
# for i,j in data.iteritems():
# 	print i,"::::::::::::",j,"<<<<<<<<<<<<<<<<"
	# dat=subjectdetails.objects.filter(collegename=i,year=j,branch="eee")
	# print dat,"}}}}}}}}}}}}}}}"
# for i in colege_name:
# 	print "college name ",i
	
# 	print data[i]
# 	for j in data[i]:
# 		print "episode is ",j
# 		subjectdetails.objects.filter(collegename=i,year=j,branch="eee")
		# year,colege_name,ee

[[[data][data]]

[[data, data]]

		[
		[[u'cbit', u'2015', 0, 0, 0], [u'cbit', u'2017', 0, 0, 0], [u'cbit', u'2016', 0, 0, 0]], 
		[[u'bsit', u'2015', 0, 0, 0], [u'bsit', u'2017', 1, 1, 1], [u'bsit', u'2016', 0, 0, 0]], 
		[[u'jntu', u'2015', 0, 0, 0], [u'jntu', u'2017', 0, 0, 0], [u'jntu', u'2016', 1, 1, 1]]
		]

		[
		[u'cbit', u'2015', 0, 0, 0], [u'cbit', u'2017', 0, 0, 0], [u'cbit', u'2016', 0, 0, 0], 
		[u'bsit', u'2015', 0, 0, 0], [u'bsit', u'2017', 1, 1, 1], [u'bsit', u'2016', 0, 0, 0], [u'jntu', u'2015', 0, 0, 0], [u'jntu', u'2017', 0, 0, 0], [u'jntu', u'2016', 1, 1, 1]]