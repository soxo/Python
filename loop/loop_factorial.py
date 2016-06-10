#!/usr/bin/python
# -*- coding:utf-8 -*-

def fact(n):
    s = 1
    for i in range(n,0,-1):
        s = i * s
    return s


print '5!: {} '.format(fact(5))
print '10!: {} '.format(fact(10))


print '*' * 40

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


for i in  range(11):
    print "%2d! = %d" % (i,factorial(i))
