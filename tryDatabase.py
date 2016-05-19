import MySQLdb

f = open("20160517/IF1609.data")
line = f.readline()
while line:
	parameters = line.split("\t")
	print line
	#print parameters[1]
	line = f.readline()
f.close()

try:
	conn=MySQLdb.connect(host='localhost', user='root', passwd='adec120', db='test', port=3306)
	cur=conn.cursor()
	cur.execute('select * from test;')
	results = cur.fetchall()
	for row in results:
		value = row[0]
		print value
	cur.close()
	conn.close()
	print "Successful"
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])

