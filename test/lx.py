#!/usr/bin/python
# -*- coding:utf-8 -*-



s = raw_input('Input the char: ')
total = 0
for i in s:
    print ord(i)
    total = total + ord(i)
print 'sum: %s' % total



s = raw_input('Input the char: ')
total = sum([(ord(i)) for i in s])
print 'sum: %s' % total


print  map(ord,s)
