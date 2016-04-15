#!/usr/bin/python
# -*- coding:utf-8 -*-



# Script Name   : find_file.py 
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  
 
  
import os,re


def find():
    fileName = raw_input('FileName: ')
    reobj = re.compile(fileName)
    for pwd,dirs,name in os.walk('/'):
        if fileName in name:
            print "%s/%s" % (pwd,fileName)
         



find()
