#!/usr/bin/python
# -*- coding:utf-8 -*-

from Tkinter import *

master = Tk()
master.title('try')
#master.geometry('350x450')

def function1():
	print 'function1'

def function2():
	print 'function2'
def function3():
	print 'function3'

buttonQuery = Button(master, text = "开始查询", command = function1)
buttonQuery.grid(padx = 80, pady = 20)

buttonChangeIns = Button(master, text= "修改订阅合约信息", command = function2)
buttonChangeIns.grid(padx = 80, pady = 20)

buttonChangeAccount = Button(master, text = "修改CTP账户", command = function3)
buttonChangeAccount.grid(padx = 80, pady = 20)

buttonQuit = Button(master, text = "退出", command = quit)
buttonQuit.grid(padx = 80, pady = 20)

mainloop()
