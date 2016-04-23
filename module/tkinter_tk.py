#!/usr/bin/python
# -*- coding:utf-8 -*-



import Tkinter


def sai():
    print "hello,world"

tk = Tkinter.Tk()
bn = Tkinter.Button(tk,text='click me',command=sai)
bn.pack()



can = Tkinter.Canvas(tk,width=500,height=500)
can.pack()
can.create_line(0,0,500,500)
can.create_rectangle(20,30,250,60)

