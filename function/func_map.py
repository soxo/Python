#!/usr/bin/python
# -*- coding:utf-8 -*-



s = [1,2,3,4]
print map(lambda x:x**2,s)


a = [1,2,3]
print map(str,a)



def add(x):
    return x + 2 

print map(add,a)

print '*' * 40


m = [1,2,3]
n = [4,5,6]
print map(lambda x,y:x+y,m,n)
