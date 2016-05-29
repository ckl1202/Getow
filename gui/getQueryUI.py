#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
from showDataUI import *

def GetTextOfEntry(Entry):
	text = Entry.get()
	return text

def GetQuery(InsEntry, TimeEntry, NumEntry):
	ins = GetTextOfEntry(InsEntry)
	beginTime = GetTextOfEntry(TimeEntry)
	num = int(GetTextOfEntry(NumEntry))
	QueryAndShowData(ins, beginTime, num)

def Query():
	root = Tk()
	root.title("查询")

	InsLabel = Label(root, text = "合约名称")
	InsLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
	InsEntry = Entry(root)
	InsEntry.grid(row = 0, column = 1, padx = 10, pady = 10)
	
	TimeLabel = Label(root, text = "开始时间")
	TimeLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
	TimeEntry = Entry(root)
	TimeEntry.grid(row = 1, column = 1, padx = 10, pady = 10)

	NumLabel = Label(root, text = "数量")
	NumLabel.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
	NumEntry = Entry(root)
	NumEntry.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	QueryButton = Button(root, text = "查询", command = lambda: GetQuery(InsEntry, TimeEntry, NumEntry))
	QueryButton.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
	QuitButton = Button(root, text = "退出", command = root.destroy)
	QuitButton.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = E)	
