"""To find the time at which a mail was received and how many mails were received in a particular hour"""
import re
try:
    #fname=input("Enter a file name: ")
    fh=open("mbox.txt")
except:
    print("ERROR Opening file")
lst=list()
lst2=list()
lst3=list()
dct=dict() 
for line in fh :
    if re.findall('^From .*',line):#line.startswith("From ") :
        lst=line.split(":")
        lst2=lst[0].split() 
        lst3.append(lst2[len(lst2)-1])
     
for hour in lst3 :
     dct[hour]=dct.get(hour,0)+1

t=sorted(dct.items())

for v,k in t :
    print(v,k)
