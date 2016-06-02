#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
import sys
sys.path.append("../kernel")
from changeDatabase import GetNowDatabase

def GetMarketData(ins, beginTime, num):
	myHost, myUser, myPassword, myDB, myPort = GetNowDatabase()
	conn = MySQLdb.connect(host=myHost, user=myUser, passwd=myPassword, db=myDB, port=int(myPort))
	cur = conn.cursor()
	command = "select * from MarketData where Instrument = '" + ins + "' and time >= '" + beginTime + "';"
	#print command 
	cur.execute(command)
	datas = cur.fetchall()
	dics = []
	if (num > len(datas)):
		num = len(datas)
	for i in range(num):
		data = datas[i]
		dic = {'InstrumentID' : data[0],
			'Time' : data[1],
			'openPrice' : data[2],
			'closePrice' : data[3],
			'highPrice' : data[4],
			'lowPrice' : data[5],
			'volume' : data[6],
			'turnover' : data[7] }
		dics.append(dic)
	cur.close()
	conn.close()
	return dics

