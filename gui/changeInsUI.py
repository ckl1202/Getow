#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *

def changeInsList():
	root = Toplevel()
	insText = Text(root)
	insText.grid()
	buttonSave = Button(root, text = "保存", command = root.destroy)
	buttonSave.grid()
	mainloop()

