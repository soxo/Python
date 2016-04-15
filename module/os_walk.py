#!/usr/bin/python
# -*- coding:utf-8 -*-



# Script Name   : os_walk.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  


import os


dirs = os.chdir(r'C:\Users\admin\python\test')
cwd = os.getcwd()
for pwd,null,fileName in os.walk(cwd):
	print fileName 

