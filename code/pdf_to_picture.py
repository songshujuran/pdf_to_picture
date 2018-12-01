#!/usr/bin/python
# -*- coding: utf-8 -*-

from pdf2image import convert_from_path
from Gui import *
import tkinter

labels = []
def try_change():
	for label in labels: 
		label.destroy()
	try:
		pages = convert_from_path(entry1.get(), 0)
		for page in pages:
			page.save(entry2.get(), 'JPEG')
		label=g.la(text='Finished!!!!')
		labels.append(label)
	except:
		label=g.la(text='Check your input and try again.检查你的输入然后再试一次')
		labels.append(label)

g = Gui()

g.geometry("800x100")
g.title('pdf to jpg')
entry1 = g.en(text="Enter the source directory.输入源文件地址(ex:'C:\github\untitled.pdf')")
entry2 = g.en(text="Enter the place you want to plave the picture.输入你想要放图片的地址(ex:'C:\github\out.jpg')")
button = g.bu(text='Begin transforming!!!!!',command=try_change)
g.mainloop()
