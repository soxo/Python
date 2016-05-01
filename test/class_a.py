#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass__ = type

class A:
    def look(self):
        self.think = 'thinking'
    def read(self,word):
        self.word = word
        self.book = 'python'
    def say(self):
        self.name = 'admin'
        print '%s read book %s' % (self.name,self.book)
        print '%s' % self.think

if __name__ == "__main__":

    a = A()
    a.read('hello')
    print a.book
    a.look()
    a.say()
    print a.name
