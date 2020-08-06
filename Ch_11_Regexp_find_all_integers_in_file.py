# Ch_11_Regexp_find_all_integers_in_file
import re
try:
    fh=open("regexp_actual.txt")
except:
    print("error")
numlist=list()

for line in fh:
    inte=re.findall('[0-9]+',line)
    if len(inte)==0 : 
        continue
    i=0
    while i<len(inte):
        num=int(inte[i])
        numlist.append(num)
        i=i+1
print(sum(numlist))