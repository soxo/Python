#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : dict_order.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 



dic = {'a':1,'b':2,'c':3}
print 'old dict: %s' % dic
key = dic.keys()
key.sort()
for i in key:
    print '%s => %s' % (i,dic[i])


print '*' * 40

dic = {'a':1,'b':2,'c':3}
print 'old dict: %s' % dic
for key in sorted(dic):
    print '%s => %s' % (key,dic[key])

