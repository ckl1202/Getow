import time
import MySQLdb

today = time.strftime("%Y-%m-%d", time.localtime())
print today

f = open("IC1609.data")
line = f.readline()
line = f.readline()
tick = 0

conn = MySQLdb.connect(host='localhost', user='root', passwd='adec1202', db='futures', port=3306)
cur = conn.cursor()
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
	tick = tick + 1
	command = "insert into CTPLastPriceData values ('IC1609', '%s', %d, %f);" % (today, tick, lastPrice)
	print command
	cur.execute(command)
	line = f.readline()

conn.commit()
cur.close()
conn.close()
f.close()
