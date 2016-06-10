#!/usr/bin/python
# -*- coding:utf-8 -*-



# Script Name   : list_fib.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 

# 斐波那契数列: 后一个数是其相邻的前两个数之和

def fib(n):
    s = [0,1]
    if n == 1:
        s.remove(1)
        return s
    elif n == 2:
        return s
    else:
        for i in range(n-2):
            s.append(s[-1] + s[-2])
        return s

print fib(1)
print fib(2) 
print fib(5)
    

print '*' * 40

def fib(n):
    s = [0,1]
    if n == 1:
        s.pop()
        return s
    elif n == 2:
        return s
    else:
        [s.append(s[i-2] + s[i-1]) for i in range(2,n)]
        return s 

print fib(1)
print fib(2)
print fib(5)

print '*' * 40

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print fib(4)
