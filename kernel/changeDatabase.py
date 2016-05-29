#!/usr/bin/python
# -*- coding:utf-8 -*-

def GetNowDatabase():
	configFile = open("../config/database.cfg", "r")
	host = configFile.readline()[:-1]
	user = configFile.readline()[:-1]
	password = configFile.readline()[:-1]
	db = configFile.readline()[:-1]
	port = configFile.readline()[:-1]
	return host, user, password, db, port

def SaveNewDatabase(host, user, password, db, port):
	configFile = open("../config/database.cfg", "w")
	configFile.write(host)
	configFile.write('\n')
	configFile.write(user)
	configFile.write('\n')
	configFile.write(password)
	configFile.write('\n')
	configFile.write(db)
	configFile.write('\n')
	configFile.write(port)
	configFile.write('\n')
	configFile.close()


