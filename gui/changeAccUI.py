#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *
import sys
sys.path.append("..kernel")
import tkMessageBox
from changeAccount import *

def GetTextOfEntry(Entry):
	text = Entry.get()
	return text

def SaveAccountEntry(BrokerEntry, InvestorEntry, PasswordEntry, AddressEntry, MarketPortEntry):
	brokerID = GetTextOfEntry(BrokerEntry)
	investorID = GetTextOfEntry(InvestorEntry)
	password = GetTextOfEntry(PasswordEntry)
	address = GetTextOfEntry(AddressEntry)
	marketPort = GetTextOfEntry(MarketPortEntry)
	SaveNewAccount(brokerID, investorID, password, address, marketPort)
	tkMessageBox.showinfo(message = "保存成功")


def changeAccount():
	root = Tk()
	root.title("修改CTP账户信息")
	brokerID, investorID, password, address, marketPort = GetNowAccount()
	BrokerLabel = Label(root, text = "经纪公司代码")
	BrokerLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
	BrokerEntry = Entry(root)
	BrokerEntry.grid(row = 0, column = 1, padx = 10, pady = 10)
	BrokerEntry.insert(0, brokerID)

	InvestorLabel = Label(root, text = "用户代码")
	InvestorLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
	InvestorEntry = Entry(root)
	InvestorEntry.grid(row = 1, column = 1, padx = 10, pady = 10)
	InvestorEntry.insert(0, investorID)

	PasswordLabel = Label(root, text = "密码")
	PasswordLabel.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
	PasswordEntry = Entry(root)
	PasswordEntry.grid(row = 2, column = 1, padx = 10, pady = 10)
	PasswordEntry.insert(0, password)
	
	AddressLabel = Label(root, text = "服务器地址")
	AddressLabel.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
	AddressEntry = Entry(root)
	AddressEntry.grid(row = 3, column = 1, padx = 10, pady = 10)
	AddressEntry.insert(0, address)
	
	MarketPortLabel = Label(root, text = "前置行情端口")
	MarketPortLabel.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = W)
	MarketPortEntry = Entry(root, text = "")
	MarketPortEntry.grid(row = 4, column = 1, padx = 10, pady = 10)
	MarketPortEntry.insert(0, marketPort)

	SaveButton = Button(root, text = "保存", command = lambda: SaveAccountEntry(BrokerEntry, InvestorEntry, PasswordEntry, AddressEntry, MarketPortEntry))
	SaveButton.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = W)
	QuitButton = Button(root, text = "退出", command = root.destroy)
	QuitButton.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = E)

