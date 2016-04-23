#!/usr/bin/python
# -*- coding:utf-8 -*-


import Tkinter

tk = Tkinter.Tk()
btn = Tkinter.Button(tk,text='Enter')
btn.pack()

canvas = Tkinter.Canvas(tk,width=500,height=500)
canvas.pack()


canvas.create_line(10,10,50,20)

