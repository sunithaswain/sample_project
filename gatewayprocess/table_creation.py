import xml.etree.ElementTree as ET
headings = ["Name","Age","Button"]
data = [
            ["sunitha","23"],
            ["anitha","25"],
            ["namitha","24"],
            ["kavitha","28"]        ]
div_root=ET.Element('html')
head=ET.SubElement(div_root,'head')
title=ET.SubElement(head,'title').text="Testing"    
div_body=ET.SubElement(div_root,'body')
table_root1=ET.SubElement(div_body,'table',border="1",cls="table")
th_root=ET.SubElement(table_root1,'tr',)
for i in headings:
    print i,"iiiiiiii"  
    td_root=ET.SubElement(th_root,'th').text=str(i)
for j in data:
    print j,"LLLLLLLLLL"
    tr_root=ET.SubElement(table_root1,'tr')
    for k in j:
        td_root=ET.SubElement(tr_root,'td').text=str(k)    

table_data = ET.tostring(div_root).replace('cls','class')
print table_data
with open("/home/sunitha/Documents/practice_projects/gatewayprocess/writedata.html","w") as cf:
    cf.write(table_data)