#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass = type

class Person:
    count = 0
    def __init__(self):
        Person.count += 1
    def say(self):
        print "HaHa,%d " % self.count


    def __del__(self):
        Person.count -= 1


a = Person()
print a.count
print a.say()
a.__del__()

print '*' * 40
b = a
print b.count
print b.say()

print '*' * 40
c = Person()
print c.count
print c.say()


print '*' * 40
print a.count
print b.count
print c.count
