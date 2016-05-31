from Tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.grid(row = 0, column = 0, padx = 10, pady = 10)

listbox.insert(END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

l2 = Listbox(master)
l2.grid(row = 0, column = 1, padx = 10, pady = 10)


mainloop()
