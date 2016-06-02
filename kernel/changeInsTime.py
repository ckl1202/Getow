#!/usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb
from changeDatabase import GetNowDatabase

def GetInsTime(insName):
	myHost, myUser, myPassword, myDB, myPort = GetNowDatabase()
	conn = MySQLdb.connect(host = myHost, user = myUser, passwd = myPassword, db = myDB, port = (int)(myPort))
	cur = conn.cursor()
	command = "select * from InsTime where Instrument = '" + insName + "' ;"
	#print command 
	cur.execute(command)
	datas = cur.fetchall()
	#print datas
	dics = []
	for item in datas:
		dic = {'beginTime' : item[1],
			'endTime' : item[2] }
		dics.append(dic)
	cur.close()
	conn.close()
	return dics

def saveInsTime(insName, times):
	if times == []:
		return
	myHost, myUser, myPassword, myDB, myPort = GetNowDatabase()
	conn = MySQLdb.connect(host = myHost, user = myUser, passwd = myPassword, db = myDB, port = (int)(myPort))
	cur = conn.cursor()
	command = "delete from InsTime where Instrument = '" + insName + "';"
	#print command 
	cur.execute(command)
	for item in times:
		command = "insert into InsTime values('" + insName \
			+ "', '" + item[0] \
			+ "', '" + item[1] + "');"
		#print command 
		cur.execute(command)
	conn.commit()
	cur.close()
	conn.close()

