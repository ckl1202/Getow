#!/usr/bin/python
# -*- coding:utf-8 -*-
import Tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.grid(sticky=tk.E+tk.W+tk.N+tk.S)
		self.createWidgets()
	def changeInsList(self):
		print "To be done"
	def createWidgets(self):
		self.quitButton = tk.Button(self, text='退出', command=self.quit)
		self.insButton = tk.Button(self, text="修改CTP订阅合约", command=self.changeInsList)
		self.insButton.grid(pady = 5, sticky=tk.E+tk.W+tk.N+tk.S)
		self.quitButton.grid(pady = 5, sticky='we')

app = Application()
app.master.title('Sample application')
app.master.geometry('200x200')
app.mainloop()
