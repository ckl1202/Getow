#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import sys
sys.path.append("../kernel")
import tkMessageBox
from changeDatabase import *

def GetTextOfEntry(Entry):
	text = Entry.get()
	return text

def SaveDatabaseEntry(HostEntry, UserEntry, PasswordEntry, DBEntry, PortEntry):
	host = GetTextOfEntry(HostEntry)
	user = GetTextOfEntry(UserEntry)
	password = GetTextOfEntry(PasswordEntry)
	db = GetTextOfEntry(DBEntry)
	port = GetTextOfEntry(PortEntry)
	SaveNewDatabase(host, user, password, db, port)
	tkMessageBox.showinfo(message = "保存成功")
	

def changeDatabase():
	root = Tk()
	root.title("修改MySQL配置")
	
	host, user, password, db, port = GetNowDatabase()
	
	HostLabel = Label(root, text = "服务器地址")
	HostLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
	HostEntry = Entry(root)
	HostEntry.grid(row = 0, column = 1, padx = 10, pady = 10)
	HostEntry.insert(0, host)
	
	UserLabel = Label(root, text = "用户名")
	UserLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
	UserEntry = Entry(root)
	UserEntry.grid(row = 1, column = 1, padx = 10, pady = 10)
	UserEntry.insert(0, user)
	
	PasswordLabel = Label(root, text = "密码")
	PasswordLabel.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
	PasswordEntry = Entry(root)
	PasswordEntry.grid(row = 2, column = 1, padx = 10, pady = 10)
	PasswordEntry.insert(0, password)

	DBLabel = Label(root, text = "数据库名")
	DBLabel.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
	DBEntry = Entry(root)
	DBEntry.grid(row = 3, column = 1, padx = 10, pady = 10)
	DBEntry.insert(0, db)
	
	PortLabel = Label(root, text = "端口号")
	PortLabel.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)
	PortEntry = Entry(root)
	PortEntry.grid(row = 4, column = 1, padx = 10, pady = 10)
	PortEntry.insert(0, port)

	SaveButton = Button(root, text = "保存", command = lambda: SaveDatabaseEntry(HostEntry, UserEntry, PasswordEntry, DBEntry, PortEntry))
	SaveButton.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)
	QuitButton = Button(root, text = "退出", command = root.destroy)
	QuitButton.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = E)	
	
#changeDatabase()
#mainloop()
