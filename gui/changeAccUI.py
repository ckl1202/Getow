#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import sys
sys.path.append("..kernel")
import tkMessageBox

def changeAccount():
	root = Tk()
	root.title("修改CTP账户信息")
	BrokerLabel = Label(root, text = "经纪公司代码")
	BrokerLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
	BrokerEntry = Entry(root, text = "9999")
	BrokerEntry.grid(row = 0, column = 1, padx = 10, pady = 10)

	InvestorLabel = Label(root, text = "用户代码")
	InvestorLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
	InvestorEntry = Entry(root)
	InvestorEntry.grid(row = 1, column = 1, padx = 10, pady = 10)

	PasswordLabel = Label(root, text = "密码")
	PasswordLabel.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
	PasswordEntry = Entry(root)
	PasswordEntry.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	AddressLabel = Label(root, text = "服务器地址")
	AddressLabel.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
	AddressEntry = Entry(root)
	AddressEntry.grid(row = 3, column = 1, padx = 10, pady = 10)
	
	MarketPortLabel = Label(root, text = "前置行情端口")
	MarketPortLabel.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)
	MarketPortEntry = Entry(root, text = "")
	MarketPortEntry.grid(row = 4, column = 1, padx = 10, pady = 10)

	SaveButton = Button(root, text = "保存")
	SaveButton.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)
	QuitButton = Button(root, text = "退出", command = root.destroy)
	QuitButton.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = E)

