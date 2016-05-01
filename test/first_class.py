#!/usr/bin/python
# -*- coding:utf-8  -*-



__metaclass__ = type


class FirstClass:
    def setdata(self,value):
        self.data = value
    def display(self):
        print self.data


class SecondClass(FirstClass):
    def display(self):
        print 'current value = %s' % self.data



class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value
    def __add__(self,other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]'  % self.data

    def mul(self,other):
        self.data *= other

if __name__ == "__main__":
    '''
    a = FirstClass()
    a.setdata('xxxxx')
    a.display()
    b = SecondClass()
    b.setdata('admin')
    b.display()
    '''
    t = ThirdClass('soxo')
    t.display()
    print t
    b = t + 'xyz'
    b.display()
    print b

    t.mul(3)
    print t

    print ThirdClass.__dict__
