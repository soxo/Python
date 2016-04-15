#!/usr/bin/python
# -*- coding:utf8 -*-



# Script Name   : leap_year.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 

year = int(raw_input('Please enter year: '))
if (year%4 == 400 or year%4 == 0 and year%100 != 0):
	print "%d is a leap year" % year
else:
	print "%d is not a leap year" % year
