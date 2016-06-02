#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
sys.path.append("../kernel")
from changeDatabase import GetNowDatabase
from changeIns import GetNowInsList
from changeInsTime import *
from Tkinter import *


def selectIns(insListbox, insTimeText):
	insName = insListbox.get(insListbox.curselection())
	insTime = GetInsTime(insName)
	insTimeText.delete(1.0, END)
	for time in insTime:
		insTimeText.insert(END, time['beginTime'])
		insTimeText.insert(END, '-')
		insTimeText.insert(END, time['endTime'])
		insTimeText.insert(END, '\n')
	

def changeInsTime():
	root = Tk()
	root.title("修改合约时间")
	insListbox = Listbox(root)
	insListbox.grid(row = 0, column = 0, padx = 10, pady = 10)
	
	insList = GetNowInsList()

	insTimeText = Text(root)
	insTimeText.grid(row = 0, column = 1)
	for item in insList:
		insListbox.insert(END, item)

	SaveButton = Button(root, text = "保存", command = root.destroy)
	SaveButton.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
	QuitButton = Button(root, text = "退出", command = root.destroy)
	QuitButton.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = E)

	insListbox.bind("<<ListboxSelect>>", lambda(event) : selectIns(insListbox, insTimeText))

changeInsTime()
mainloop()
