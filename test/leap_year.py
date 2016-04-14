#!/usr/bin/python
# -*- coding:utf8 -*-



year = int(raw_input('Please enter year: '))
if (year%4 == 400 or year%4 == 0 and year%100 != 0):
	print "%d is a leap year" % year
else:
	print "%d is not a leap year" % year
