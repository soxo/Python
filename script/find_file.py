#!/usr/bin/python
# -*- coding:utf-8 -*-


import os,re


def find():
    fileName = raw_input('FileName: ')
    reobj = re.compile(fileName)
    for pwd,dirs,name in os.walk('/'):
        if fileName in name:
            print "%s/%s" % (pwd,fileName)
         



find()
