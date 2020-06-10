import json
import urllib
import urllib.request, urllib.parse, urllib.error
import ssl
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_619223.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx) #ssl
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	number = int(item["count"])
	count = count + number
print (count)
