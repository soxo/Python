#!/usr/bin/python
# -*- coding:utf-8 -*-


x = 100

def f1():
    x = 80
    def f2():
        print x
    f2()
f1()

