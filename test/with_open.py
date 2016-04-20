#!/usr/bin/python
# -*= coding:utf-8 -*-


'''
with open('with_open.txt','r+') as text:
    print text.read().rstrip()
'''


for i in open('with_open.txt','r+').readline():
    print i,



for line in open('with_open.txt','r'):
    print line.strip()




