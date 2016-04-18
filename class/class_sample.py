#!/usr/bin/python
# -*- coding:utf-8 -*-



class Person:
    
    Email = 'zd_feeling@126.com'
    Language = 'Python'

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def sai(self):
        print  "Hello,{1} I'm {0}".format(self.name,self.Language)

print Person.Email
print Person().Email

Tom = Person()
John = Person()
Tom.setName('Tom')
John.setName('John')

print '*' * 40

print Tom.sai()
print Tom.getName()
print Tom.name
print Tom.Email
print Person.Email
print Person().Email

Tom.name = 'admin'
print Tom.name
print Tom.sai()


Tom.Email = 'Unknow'
print Tom.Email
print Person.Email

print '*' * 40

print John.name
print John.Email

