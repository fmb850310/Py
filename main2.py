#!/usr/bin/python3
import http.client
import csv
from pyquery import PyQuery as pq

hostname = "tw.stock.yahoo.com"
linkformat = "/q/ts?s=%d"
requestMethod = "GET"
selector = "table[border='0'][cellpadding='4'][cellspacing='1'][width='100%'] tr:nth-child(2) td"

fp = open('filename.txt', "r")
f = open('today1.csv', 'w', encoding = 'big5')
line = fp.readline()
while line:
	stockID = int(line)
	link = linkformat % int(stockID)
	print(stockID)
	req = http.client.HTTPSConnection(hostname)
	req.request(requestMethod, link)
	resp = req.getresponse().read()
	stock_str = "%d" % stockID
	d = pq(resp)
	f.write(stock_str)
	for el in d(selector):
		f.write(",")
		f.write(el.text)
	f.write("\n")
	line = fp.readline()
fp.close()
f.close()