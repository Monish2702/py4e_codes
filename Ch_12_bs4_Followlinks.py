import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL : ')
count=int(input("Enter count :"))
p=int(input("Enter position :"))

print('Retrieving : ',url)

for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    c=0
    for tag in tags:
        c+=1
        if c==p:
           url=tag.get('href',None)
           print('Retrieving : ',url)
           c=0 
           break    

    
    # Sample similar code from Github   
    
# #Data Collection
# link = input('Enter URL: ')
# cont = int(input('Enter count: '))
# line = int(input('Enter position: '))



# # print('Retrieving: %s' % link)
# for i in range(0, cont):
#     html = urllib.request.urlopen(link, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
    
#     tags = soup('a')
#     cn = 0
#     ps = 0
#     for tag in tags:
#         ps += 1
#         if ps == line:
#             print('Retrieving: %s' % str(tag.get('href', None)))
#             link = str(tag.get('href', None))
#             ps = 0
#             break
 
 
   
  