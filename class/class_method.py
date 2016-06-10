#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass__  = type

class A:
    
    def say(self):
        print "Hello"

    @classmethod
    
    def look(clss):
        print "class method"

    @staticmethod
    
    def think():
        print "static method"


class B(A):
    
    @classmethod
    
    def look(clss):
        print "class method B"


if __name__ == "__main__":
    
    f = A()
    A.say(f)
    f.say()
    f.look()
    
    A.look()
    
    f.think()
    A.think()

    B.look()

    



