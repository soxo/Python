#!/usr/bin/python
# -*- coding:utf-8 -*-



__metaclass__ = type



class Person:
    __name = 'admin'
    def __init__(self):
        self.me = 'xxxxx'

    def read(self):
        self.page = 190
        print "%s  %d" % (self.me,self.page)

xiao = Person()
print xiao.me
#print xiao.page
xiao.read()
