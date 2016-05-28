#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import MySQLdb
import sys
sys.path.append("../kernel")
from changeIns import GetNowInsList

def CheckDataValid(parameter, validTimes):
        if (parameter['lastPrice'] > 1000000) or (parameter['lastPrice'] < -1000000):
		return False
	if (parameter['bidPrice'] > 1000000) or (parameter['bidPrice'] < -1000000):
		return False
	if (parameter['askPrice'] > 1000000) or (parameter['askPrice'] < -1000000):
		return False
	for times in validTimes:
		if times[0] <= parameter['time'] and parameter['time'] < times[1]: 
			return True
	return False


today = time.strftime("%Y-%m-%d", time.localtime())
conn = MySQLdb.connect(host='localhost', user='root', passwd='adec1202', db='futures', port=3306)
cur = conn.cursor()


insList = GetNowInsList()
for ins in insList:
	filename = "../dataGetter/%s.data" %ins
	f = open(filename, "r")
	tick = 0
	command = "select beginTime, endTime from InsTime where Instrument = '%s'" %ins
	cur.execute(command)
	validTimes = cur.fetchall()
	line = f.readline()
	datas = []

	while line:
		parameters = line.split()
		lastPrice = float(parameters[0])
		bidPrice = float(parameters[1])
		askPrice = float(parameters[2])
		bidVolume = int(parameters[3])
		askVolume = int(parameters[4])
		volume = int(parameters[5])
		turnover = float(parameters[6])
		openinterest = int(float(parameters[7]))
		time = parameters[8]
		#time.strptime(parameters[8], '%H:%M:%S')
		parameter = {'InstrumentID' : ins,
				'lastPrice' : lastPrice,
				'bidPrice' : bidPrice,
				'askPrice' : askPrice,
				'bidVolume' : bidVolume, 
				'askVolume' : askVolume,
				'volume' : volume,
				'turnover' : turnover,
				'openinterest' : openinterest, 
				'time' : time}
		
		
		
		if (CheckDataValid(parameter, validTimes)):
			datas.append(parameter)
		#command = "insert into CTPLastPriceData values ('%s', '%s', %d, %f);" % (ins, today, tick, lastPrice)
		#cur.execute(command)
		#command = "insert into CTPBidData values ('%s', '%s', %d, %f, %d);" %(ins, today, tick, bidPrice, bidVolume)
		#cur.execute(command)
		#command = "insert into CTPAskData values ('%s', '%s', %d, %f, %d);" %(ins, today, tick, askPrice, askVolume)
		#cur.execute(command)
		#command = "insert into CTPDealData values ('%s', '%s', %d, %d, %f);" %(ins, today, tick, volume, turnover)
		#cur.execute(command)
		#command = "insert into CTPPosData values ('%s', '%s', %d, %d);" %(ins, today, tick, openinterest)
		#cur.execute(command)
		#command = "insert into CTPTickTime values ('%s', '%s', %d, '%s');" %(ins, today, tick, time)
		#cur.execute(command)
		line = f.readline()
	
	if (len(datas) != 0):
		prevData = datas[0]
		openPrice = prevData['lastPrice']
		highPrice = openPrice
		lowPrice = openPrice
		volume = prevData['volume']
		turnover = prevData['turnover']
		for i in range(1, len(datas)):
			nowData = datas[i]
			if prevData['time'][:5] == nowData['time'][:5]:
				if nowData['lastPrice'] > highPrice:
					highPrice = nowData['lastPrice']
				if nowData['lastPrice'] < lowPrice:
					lowPrice = nowData['lastPrice']
				volume = nowData['volume']
				turnover = nowData['turnover']
			else:
				closePrice = prevData['lastPrice']
				time = today + '-' + prevData['time'][:5]
				print time, 
				command = "insert into MarketData values ('%s', '%s', %f, %f, %f, %f, %d, %f);" \
					% (ins, time, openPrice, closePrice, highPrice, lowPrice, volume, turnover)
				cur.execute(command)
				lowPrice = nowData['lastPrice']
				highPrice = nowData['lastPrice']
				openPrice = nowData['lastPrice']
			prevData = nowData
		time = today + '-' + prevData['time'][:5]
		command = "insert into MarketData values ('%s', '%s', %f, %f, %f, %f, %d, %f);" \
			% (ins, time, openPrice, closePrice, highPrice, lowPrice, volume, turnover)
		cur.execute(command)

					
conn.commit()
cur.close()
conn.close()
f.close()
