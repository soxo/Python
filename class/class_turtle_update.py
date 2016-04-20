#!/usr/bin/python
# -*- coding:utf-8 -*-


import turtle

class Fork: 
    def __init__(self,angle,forward): 
        self.angle = angle
        self.forward = forward
        
    def up(self,step):
        self.step = step
        t = turtle.Pen()
        t.forward(self.forward)
        t.left(self.angle)
        t.forward(step)
        t.right(self.angle)
        t.forward(step)

    def down(self,step):
        self.step = step
        m = turtle.Pen()
        m.forward(self.forward)
        m.right(self.angle)
        m.forward(step)
        m.left(self.angle)
        m.forward(step)


a = Fork(90,200)
a.up(100)
a.down(100)

b = Fork(90,160)
b.up(150)
b.down(150)

