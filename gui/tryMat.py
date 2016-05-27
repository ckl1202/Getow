import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from matplotlib.finance import candlestick
from matplotlib.dates import date2num, MinuteLocator, DateFormatter
from datetime import datetime

date1 = '09:30'
date1 = date2num(datetime.strptime(date1, "%H:%M"))
date2 = '09:31'
date3 = '09:32'
date4 = '09:33'
date5 = '09:34'
date2 = date2num(datetime.strptime(date2, "%H:%M"))
date3 = date2num(datetime.strptime(date3, "%H:%M"))
date4 = date2num(datetime.strptime(date4, "%H:%M"))
date5 = date2num(datetime.strptime(date5, "%H:%M"))


openPrice = [2916.8, 2922.6, 2921.4, 2922.6, 2920.8]
highPrice = [2922.6, 2922.6, 2922.8, 2922.6, 2920.8]
lowPrice = [2915.8, 2920.0, 2921.4, 2920.8, 2920.8]
closePrice = [2922.6, 2921.4, 2922.6, 2920.8, 2920.8]
#candlestick: date open close high low
minuteFormatter = DateFormatter('%H:%M')
price = [(date1, 2916.8, 2922.6, 2922.6, 2915.8),
	(date2, 2922.6, 2921.4, 2922.6, 2920.0),
	(date3, 2921.4, 2922.6, 2922.8, 2921.4),
	(date4, 2922.6, 2920.8, 2922.6, 2920.8),
	(date5, 2920.8, 2920.8, 2920.8, 2920.8)]

fig = plt.figure(figsize = (18, 9))
ax = fig.add_subplot(2, 1, 1)
ax.xaxis.set_major_locator(MinuteLocator())
ax.xaxis.set_major_formatter(minuteFormatter)
bx = fig.add_subplot(2, 1, 2)
candlestick(ax, price, width = 0.000005, colorup = 'r', colordown = 'g')
candlestick(bx, price, width = 0.07, colorup = 'r', colordown = 'g')
ax.autoscale_view()
plt.show()



