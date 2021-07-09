#!/usr/bin/python3
#import http.client
import requests
import csv
from pyquery import PyQuery as pq

protocol = "https"
#hostname 目標URL host
hostname = "tw.stock.yahoo.com"
#linkformat 股號 Querystring 
linkformat = "/q/ts?s=%s"
requestMethod = "GET"
#sekector html DOM 選擇器
selector = "table[border='0'][cellpadding='4'][cellspacing='1'][width='100%'] tr:nth-child(4) td"
#fp 股票號碼
fp = open('filename.txt', "r")
#f 寫入用檔案
f = open('today1.csv', 'w', encoding = 'big5')
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