#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : list_sum.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  

#求两个列表之和

a = [1,2,3]
b = [4,5,6]

for i in a:
    for k in b:
        print a[i-1]+ b[i-1]
        break

                    


print [x+y for x,y in zip(a,b)]


for i in range(len(a)):
    print a[i]+b[i]


print '*' * 40


print map(lambda x,y:x+y,a,b)
