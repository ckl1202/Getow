import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from matplotlib.finance import candlestick
from matplotlib.dates import date2num, MinuteLocator, DateFormatter
from datetime import datetime
import sys
sys.path.append("../kernel")
from showData import GetMarketData

#candlestick: date open close high low
minuteFormatter = DateFormatter('%H:%M')

dics = GetMarketData('IF1609', '2016-05-28-09:30', '2016-05-28-11:30')
datas = []
labels = []
#i = 600000
for item in dics:
	data = []
	data.append(date2num(datetime.strptime(item['Time'][-5:], "%H:%M")))
	#print data[0]
	#data.append(i)
	#i = i + 0.001
	labels.append(item['Time'][-5:])
	data.append(item['openPrice'])
	data.append(item['closePrice'])
	data.append(item['highPrice'])
	data.append(item['lowPrice'])
	datas.append(data)

fig = plt.figure(figsize = (18, 9))
ax = fig.add_subplot(2, 1, 1)
ax.xaxis.set_major_locator(MinuteLocator(range(60), 10))
ax.set_xlim([date2num(datetime.strptime('09:30', "%H:%M")), date2num(datetime.strptime('11:30', "%H:%M"))])
ax.xaxis.set_major_formatter(minuteFormatter)
bx = fig.add_subplot(2, 1, 2)

#ax.xaxis.set_ticklabels(labels)
candlestick(ax, datas, width = 0.0004, colorup = 'r', colordown = 'g')
#ax.xaxis.set_ticks(labels)
for label in ax.xaxis.get_ticklabels():
	label.set_rotation(45)
#ax.autoscale_view()
plt.show()


print 'test'
