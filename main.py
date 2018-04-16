import http.client
from pyquery import PyQuery as pq

hostname = "tw.stock.yahoo.com"
stockID = 2329
link = "/q/ts?s=%d" % stockID
selector = "table[border='0'][cellpadding='4'][cellspacing='1'][width='100%'] tr:nth-child(2) td"

req = http.client.HTTPSConnection(hostname)
req.request("GET", link)
resp = req.getresponse().read()

d = pq(resp)
for el in d(selector):
    print(el.text)