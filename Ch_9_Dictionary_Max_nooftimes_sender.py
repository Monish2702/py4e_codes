#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
try:
    fname=input("Enter Filename : ")
    fh=open(fname)
except:
    print("ERROR")
count=dict()
l=list()
for line in fh :
    if line.startswith("From "):
        lst=line.split()
        l.append(lst[1])
        
    else:
        continue
for word in l:
    count[word]=count.get(word,0)+1

bigcount=None
bigword=None
for word,c in count.items():
    if bigcount is None  or c>bigcount:
        bigword=word
        bigcount=c
print('\n')
print(bigword,bigcount)
