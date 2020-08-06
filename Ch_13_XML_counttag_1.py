import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as et 
import ssl

# ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter location : ')
print('Retreiving :',url)
html = urllib.request.urlopen(url, context=ctx).read()
print('Retreived',len(html),'Characters')
stuff=et.fromstring(html)
lst=stuff.findall('comments/comment')
print(len(lst))
s=0
for i in lst:
    x=i.find('count').text
    s=s+int(x)
print('sum is :',s)