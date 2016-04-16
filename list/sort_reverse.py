#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : sort_reverse.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 


x = [5,3,6,9,7]
print 'old x: %s'  % x
y = x.sort()
print 'new x: %s'  % x
print 'y: %s'  % y


print '*' * 40

x = [5,3,6,9,7]
print 'old x: %s'  % x
y = sorted(x)
print 'new x: %s'  % x
print 'y: %s'  % y


print '-' * 40

x = [5,3,6,9,7]
y = x[:]
print 'old x: %s'  % x
x.sort()
print 'new x: %s'  % x
print 'y: %s'  % y


print '#' * 40


x = [5,3,6,9,7]
y = x
print 'old x: %s'  % x
x.reverse()
print 'new x: %s'  % x
print 'y: %s'  % y

print '+' * 40


x = [5,3,6,9,7]
print 'old x: %s'  % x
y = list(reversed(x))
print 'new x: %s'  % x
print 'y: %s'  % y

