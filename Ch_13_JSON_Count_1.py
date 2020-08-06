import urllib.request,urllib.parse,urllib.error
import json
import ssl

# ignore ssl certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter location : ')
print('Retreiving :',url)
html = urllib.request.urlopen(url, context=ctx).read()
print('Retreived',len(html),'Characters')
j=json.loads(html)
s=0
for i in j['comments']:
    s=s+i['count']
print("Sum is :",s)