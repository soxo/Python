#!/usr/bin/python
# -*- coding:utf-8 -*-


import os


dirs = os.chdir(r'C:\Users\admin\python\test')
cwd = os.getcwd()
for pwd,null,fileName in os.walk(cwd):
	print fileName 

