#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
sys.path.append("../kernel")
from changeDatabase import GetNowDatabase
from changeIns import GetNowInsList
from changeInsTime import *
from Tkinter import *
import tkMessageBox

def selectIns(insListbox, insTimeText, insTime):
	global nLine
	if (nLine != -1):
		newTime = insTimeText.get(1.0, END)
		insTime[nLine] = newTime
	nLine = insListbox.curselection()[0]
	insTimeText.delete(1.0, END)
	insTimeText.insert(END, insTime[nLine])
	
def saveIns(insList, insTime):
	print insList
	for i in range(len(insTime)):
		#获取这个合约的时间
		thisInsTime = insTime[i]
		#按照回车分隔
		thisInsTime = thisInsTime.split('\n')
		#去除无效的行
		for j in range(len(thisInsTime) - 1, -1, -1):
			if (thisInsTime[j] == ''):
				del thisInsTime[j]
		#对于所有的行，放入一个时间数据中
		times = []
		for time in thisInsTime:
			#将开始时间和结束时间分开
			result = time.split('-')
			newTime = [result[0], result[1]]
			times.append(newTime)
		saveInsTime(insList[i], times)
		#print times
	tkMessageBox.showinfo(message = "保存成功")
			

def changeInsTime():
	root = Tk()
	root.title("修改合约时间")
	insListbox = Listbox(root)
	insListbox.grid(row = 0, column = 0, padx = 10, pady = 10)
	
	insList = GetNowInsList()

	insTimeText = Text(root)
	insTimeText.grid(row = 0, column = 1)
	insTime = []
	for item in insList:
		insListbox.insert(END, item)
		thisInsTime = GetInsTime(item)
		insStr = ''
		for time in thisInsTime:
			insStr = insStr + time['beginTime'] + '-' + time['endTime'] + '\n'
		insTime.append(insStr)


	SaveButton = Button(root, text = "保存", command = lambda: saveIns(insList, insTime))
	SaveButton.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
	QuitButton = Button(root, text = "退出", command = root.destroy)
	QuitButton.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = E)

	insListbox.bind("<<ListboxSelect>>", lambda(event) : selectIns(insListbox, insTimeText, insTime))

nLine = -1
changeInsTime()
mainloop()
