#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass__ = type


class home:

    def __init__(self,x):
        self.x = x
    def set_x(self):
        self.x = 400
    def print_x(self):
        print self.x
    def print_a(self,a):
        self.a = a
        print a
        

if __name__ == "__main__":
    v = home(200)
    print v.x
    v.print_x()
    v.print_a(1000)
    print v.a
    

