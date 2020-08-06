# Use words.txt as the file name
try:
     fname = input("Enter file name: ")
except:
    print("Enter correct file name")

fh = open(fname)
for i in fh:
    j=i.upper()
    print(j.rstrip())
