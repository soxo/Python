#!/usr/bin/python
# -*- coding:utf-8 -*-



__metalclass__ = type

class Person:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print "Hello,I'm %s"  % self.name



p = Person()
p.set_name('admin')
print p.get_name()
p.greet()
Person.greet(p)


print '*' * 40


class A:
    a = 0
    def say(self):
        self.a += 1


soxo = A()
soxo.say()
print A.a
print soxo.a

admin = A()
admin.say()
print A.a
print admin.a




