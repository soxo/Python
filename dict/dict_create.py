#!/usr/bin/python
# -*- coding:utf-8 -*-



# 创建字典的方法



dic1 = {'a':1,'b':2} 

dic2 = dict([('a',1),('b',2),['c',3]]) 

dic3 = dict(a=1,b=2,c='admin')

dic4 = {}.fromkeys(['a','b']) 

dic5 = {}.fromkeys(('a','b'),'admin')

dic6 = {}.fromkeys('admin',1) 

dic7 = dict.fromkeys(range(10),'admin')

print '''
{0}

{1}

{2}

{3}

{4}

{5}

{6}

'''.format(dic1,dic2,dic3,dic4,dic5,dic6,dic7)
