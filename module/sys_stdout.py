#!/usr/bin/python
# -*- coding:utf-8 -*-

'''

from __future__ import print_function
import sys

temp = sys.stdout

sys.stdout = open('sys_stdout.txt','a')

print ('sys.stdout,write!')

sys.stdout.close()

sys.stdout = temp

print ('*' * 40)

print (open('sys_stdout.txt','r').read())

'''

log = open('sys_stdout.txt','a')
print >> log,'python',"\nhello,world"
print 'don\'t'
log.close()
