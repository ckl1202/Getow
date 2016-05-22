#!/usr/bin/python
# -*- coding:utf-8 -*-

def GetNowInsList():
	insFile = open("../dataGetter/insList.in", "r")
	a = int(insFile.readline())
	insList = []
	for i in range(0, a):
		str = insFile.readline()
		str = str[:-1]
		insList.append(str)
	insFile.close()
	return insList

def SaveNowIns(insList):
	insFile = open("../dataGetter/insList.in", "w")
	insFile.write(str(len(insList)))
	insFile.write('\n')
	for item in insList:
		insFile.write(item)
		insFile.write('\n')
	insFile.close()


