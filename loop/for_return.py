#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : sort_reverse.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  

#return会跳出内外层循环

def func(x,*arg):
    print x
    result = x
    print arg
    for k in range(3):
        for i in arg:
            result += i
            return result

    print  k

print func(1,2,3,4,5,6,7,8,9)

