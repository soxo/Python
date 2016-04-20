#!/usr/bin/python
# -*- coding:utf -8

# Script Name   : sort_reverse.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  


import copy


m = ['ab',1,2,3]
n = m
m[1] = 2
print m,n

print '*' * 40

j = ['ab',1,2,3]
k = copy.copy(j)
j[1] = 2
print j,k

print '*' * 40

s = ['ab',1,2,3,['a','b']]
t = copy.copy(s)
u = copy.deepcopy(s)
s[1] = 2
s[4][0] = 4

print s,t,u

print '*' * 40

class Person:
    head = 'a'
    ear = 'b'
    def hit(self):
        self.shoot = 'dead'
        print "Hit the people"


p1 = Person()
p2 = p1
p3 = copy.copy(p1)
p1.head = 'admin'
print p1.head,p2.head,p3.head



two = [p1,p2]
print two[0].head,two[1].head
copyTwo = copy.copy(two)
copyTwo[0].head = 'python'
print p1.head,p2.head,copyTwo[0].head



    
