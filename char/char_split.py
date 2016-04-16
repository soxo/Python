#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : char_split.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  


f = open('/etc/passwd').readline()
print f.strip().split(':')



string = [i for i in open('/etc/passwd').readline().strip().split(':')]
print string
