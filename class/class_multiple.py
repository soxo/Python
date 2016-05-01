#!/usr/bin/python
# -*- coding:utf-8 -*-


#新类多重继承顺序为广度优先，旧类为深度优先。


__metaclass__ = type


class Person:
    def __init__(self,name):
        self.name = "I am a person"
        
    def eat(self):
        print "Person eat"

    def say(self):
        print "Hello,world"

class Women(Person): 
    def eat(self):
        print "Women eat"

class Test:
    def eat(self):
        print "Myself eat"

class Girl(Women,Person):
    def say(self):
        print "Girl say"

class HotGirl(Girl,Test):
    def say(self):
        print "HotGirl say,%s" % self.name


if __name__ == "__main__":
    yangming = HotGirl('yangming')
    yangming.eat()
    yangming.say()
    
# yangming.eat搜索顺序:首先查找HotGirl类本地有没有eat，如果没有，搜索Girl中有没有eat,如果没有，搜索Girl的父类Women有没有，如果有就打印。

 
