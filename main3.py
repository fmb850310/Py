#!/usr/bin/python3
#import http.client
import requests
import csv
from pyquery import PyQuery as pq

protocol = "https"
hostname = "tw.stock.yahoo.com"
linkformat = "/q/ts?s=%s"
requestMethod = "GET"
selector = "table[border='0'][cellpadding='4'][cellspacing='1'][width='100%'] tr:nth-child(2) td"

fp = open('filename.txt', "r")
f = open('today1.csv', 'w', encoding = 'big5')
f.write("股號")
f.write(",")
f.write("時間")
f.write(",")
f.write("買進")
f.write(",")
f.write("賣出")
f.write(",")
f.write("成交價")
f.write(",")
f.write("漲跌")
f.write(",")
f.write("單量")
f.write(",")
f.write("\n")
line = fp.readline()
while line:
	stockID = line.strip(" \t\n\r")
	link = linkformat % stockID
	print(stockID)
	#req = http.client.HTTPSConnection(hostname)
	#req.request(requestMethod, link)
	#resp = req.getresponse().read()
	r = requests.get("%s://%s%s" % (protocol, hostname, link))
	resp = r.text
	d = pq(resp)
	f.write(stockID)
	for el in d(selector):
		f.write(",")
		f.write(el.text)
	f.write("\n")
	line = fp.readline()
fp.close()
f.close()