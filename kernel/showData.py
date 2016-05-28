#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb

def GetMarketData(ins, beginTime, endTime):
	conn = MySQLdb.connect(host='localhost', user='root', passwd='adec1202', db='futures', port=3306)
	cur = conn.cursor()
	command = "select * from MarketData where Instrument = '" + ins + "' and time >= '" + beginTime + "' and time <= '" + endTime + "';"
	#print command 
	cur.execute(command)
	datas = cur.fetchall()
	dics = []
	for i in range(len(datas)):
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
	return dics
		


GetMarketData('IF1609', '2016-05-28-10:00', '2016-05-28-11:30')
