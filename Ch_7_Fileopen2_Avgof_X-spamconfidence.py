s=0
count=0
try:
    fh=input("Enter a filename:\n")
except :
    print("ERROR")
f=open(fh)
for i in f :
    if not i.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        count=count+1
        c=i.find('0')
        x=(float(i[c:]))
        s=s+x
print("Average spam confidence:",s/count)
