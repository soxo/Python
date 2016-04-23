#!/usr/bin/python
# -*- coding:utf-8 -*-




L = [1,2,4,8,16,32,64]
i = 0
X = 5
while i < len(L):
    if 2 ** X == L[i]:
        print ('at index',i)

    else:
        print (i,'not found')

    i += 1


