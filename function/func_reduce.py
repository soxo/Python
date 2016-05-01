#!/usr/bin/python
# -*- coding:utf-8 -*-




#横向逐个运算


s = [1,2,3,4,5]
print reduce(lambda x,y:x+y,s)


print reduce(lambda x,y:x*y,s)
