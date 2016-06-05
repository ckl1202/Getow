# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from matplotlib.finance import candlestick
from matplotlib.dates import date2num
from datetime import datetime
import sys
sys.path.append("../kernel")
from showData import GetMarketData

def QueryAndShowData(ins, beginTime, num):
	dics = GetMarketData(ins, beginTime, num)
	datas = []
	i = 1
	for item in dics:
		data = []
		data.append(i)
		i = i + 1
		data.append(item['openPrice'])
		data.append(item['closePrice'])
		data.append(item['highPrice'])
		data.append(item['lowPrice'])
		datas.append(data)

	fig = plt.figure(figsize = (18, 9))
	ax = fig.add_subplot(211)
	candlestick(ax, datas, width = 0.4, colorup = 'r', colordown = 'g')
	ax.autoscale_view()

	volumeX = fig.add_subplot(212)
	datas = []
	index = []
	i = 1
	for item in dics:
		index.append(i)
		i = i + 1
		datas.append(item['volume'])
	volumeX.set_xlim(0, num)
	plt.bar(index, datas, 0.5, color = 'r', label = '成交量')
		
	plt.show()
