from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
c = 0
sum = 0
for tag in tags:
    d = tag.contents[0]
    d = int(d)
    sum = sum + d
    c = c + 1

print("Count ",c)
print("Sum ",sum)
