#!/bin/usr/python
# -*- coding:utf-8 -*-
import time
import MySQLdb
import sys
sys.path.append("../kernel")
from changeIns import GetNowInsList

def CheckDataValid(parameters):
        if (parameters['lastPrice'] > 1000000) or (parameters['lastPrice'] < -1000000):
		return False
	if (parameters['bidPrice'] > 1000000) or (parameters['bidPrice'] < -1000000):
		return False
	if (parameters['askPrice'] > 1000000) or (parameters['askPrice'] < -1000000):
		return False
	return True


today = time.strftime("%Y-%m-%d", time.localtime())
conn = MySQLdb.connect(host='localhost', user='root', passwd='adec1202', db='futures', port=3306)
cur = conn.cursor()


insList = GetNowInsList()
for ins in insList:
	filename = "../dataGetter/%s.data" %ins
	f = open(filename, "r")
	line = f.readline()
	line = f.readline()
	tick = 0

	while line:
	#从文件中获取数据
		parameters = line.split()
		lastPrice = float(parameters[0])
		bidPrice = float(parameters[1])
		askPrice = float(parameters[2])
		bidVolume = int(parameters[3])
		askVolume = int(parameters[4])
		volume = int(parameters[5])
		turnover = float(parameters[6])
		openinterest = int(float(parameters[7]))
		time.strptime(parameters[8], '%H:%M:%S')
		parameters = {'InstrumentID' : ins,
				'lastPrice' : lastPrice,
				'bidPrice' : bidPrice,
				'askPrice' : askPrice,
				'bidVolume' : bidVolume, 
				'askVolume' : askVolume,
				'volume' : volume,
				'turnover' : turnover,
				'openinterest' : openinterest, 
				'time' : time}
	#
	#清洗数据
		if (not CheckDataValid(parameters)):
			line = f.readline
			continue
		tick = tick + 1
		command = "insert into CTPLastPriceData values ('IC1609', '%s', %d, %f);" % (today, tick, lastPrice)
		print command
		cur.execute(command)
		line = f.readline()

conn.commit()
cur.close()
conn.close()
f.close()
