#!/usr/bin/python
# -*- coding:utf-8 -*-



# Script Name   : collections_ordereddict.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  



import collections

dic = collections.OrderedDict([('a',1),('b',2),('c',3)])
print 'Key: %s'  % dic.keys()
print 'Values: %s' % dic.values()
print 'Items: %s'   % dic.items()
print  'a: %s'       % dic['a']







