#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass__ = type


class Old:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def Say(self):
        print "Hello,world"


class New(Old):
    def __init__(self,n,color,name):
        super(New,self).__init__(color,name)
        self.n = n
    
    def Say(self):
        super(New,self).Say()
        print "How mang: %d" % self.n
        print "Color: %s" % self.color



if __name__ == "__main__":
    xiaoxiao = New(12,'red','xiaoxiao')
    xiaoxiao.Say()
