#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : list_enumerate.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  




m = ['a','b','c']
n = m[:]
for j,k in enumerate(m):
    m[j] = '%d:%s' % (j,k)
    
print m




s = [ ('%d:%s' % (i,o) ) for i,o in enumerate(n)]
print s
    



def enum(a,b):
    return '%d:%s' %(a,b)

t = [enum(a,b) for a,b in enumerate(n)]
print t
