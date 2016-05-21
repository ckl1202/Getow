#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import sys
sys.path.append("../kernel")
from changeIns import *
import tkMessageBox

def GetInsText(insText):
	insList = insText.get(1.0, END)
	insList = insList.split('\n')
	for i in range(len(insList) - 1, -1, -1):
		if (insList[i] == u''):
			del insList[i]
	return insList
	

def SaveInsText(insText):
	insList = GetInsText(insText)
	print insList
	tkMessageBox.showinfo(message = "保存成功")

def changeInsList():
	root = Tk()
	insText = Text(root, width = 30, height = 15)
	insText.grid(columnspan = 2)
	buttonSave = Button(root, text = "保存", command = lambda: SaveInsText(insText))
	buttonSave.grid()
	buttonQuit = Button(root, text = "退出", command = root.destroy)
	buttonQuit.grid(row = 1, column = 1)

	insList = GetNowInsList()
	for ins in insList:
		insText.insert(END, ins)
		insText.insert(END, '\n')
	

changeInsList()
mainloop()
