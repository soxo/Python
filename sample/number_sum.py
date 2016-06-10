#!/usr/bin/python
# -*- coding:utf-8 -*-


# 求从1加到100结果


s = 0
for i in range(1,101):
    s = s + i
print s


print '*' * 40

def total(n):
    if n == 1:
        return 1
    else:
        return n + total(n-1)

    
print total(100)
