#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : imp_reload.py 
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :


import imp,collections_ordereddict

print '*' * 40
import collections_ordereddict
print '*' * 40

imp.reload(collections_ordereddict)                     # python3.0

print '-'*40

exec(open('collections_ordereddict.py').read())         # python3.0

print '#'*40

execfile('collections_ordereddict.py')
