#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : in_get.py 
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  


# setdefault与get类似，还能在字典中不含有给定键的情况下设定相应的键值


dic = {'soxo':'one','admin':'two','python':'three'}
print 'linux' in dic
print 'soxo' in dic


print dic.get('linux','nothing...')
print dic.get('soxo','nothing......')

print '*' * 40

m = dic['linux'] if 'linux' in dic else 'nothing...'
print m

n = dic['soxo'] if 'soxo' in dic else 'nothing.....' 
print n

print  '-' * 40
d =  'soxo' in dic and dic['soxo'] or 'nothing...'
print d 
