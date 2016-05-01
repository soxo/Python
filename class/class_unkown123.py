#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass__ = type


class Person:
    def set_name(self,name):
        self.name = name
        self.tall = 180
    
    def read(self):
        self.page = 20
if __name__ == "__main__":
    x = Person()
    x.set_name('admin') 
    print x.name
    print x.tall
#    print x.page
