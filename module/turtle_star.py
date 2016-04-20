#!/usr/bin/python
# -*- coding:utf-8 -*-


import turtle,time


t = turtle.Pen()
for i in range(0,5):
    t.color(1,0,0)
    t.begin_fill()
    t.forward(160)
    t.right(144)
    time.sleep(1)
else:
    t.end_fill()


t.reset()
for i in range(0,38):
    t.forward(160)
    t.right(170)
    time.sleep(1)


t.reset()
t.color(0,1,0)
t.begin_fill()
t.circle(60)
t.end_fill()
