#!/usr/bin/python
# -*- coding:utf-8 -*-




import sys



print
print "\t'{}{}'.format('abc','efg') => "  ,       '{}{}'.format('abc','efg')
print "\t'{}>{}'.format('abc','efg') => "   ,     '{}>{}'.format('abc','efg')
print "\t'{0}'.format('root') => "   ,            '{0}'.format('root')
print "\t'{1}.{0}'.format('world','hello') => " , '{1}.{0}'.format('world','hello')
print "\t'{0[0]}'.format(['a','b','c']) => "   ,  '{0[0]}'.format(['a','b','c'])
print "\t'{a}+{b}'.format(a=10,b=15) => "   ,     '{a}+{b}'.format(a=10,b=15)
#print '{0}.{1}'.format('sys','platform')
print
print "\tdic = {'a':1,'b':['soxo','python',123456]}"
dic = {'a':1,'b':['soxo','python',123456]}
print "\t'{0[a]:>015}:,{0[b][1]}'.format(dic) 向右对齐，不够15位补0=> "   ,   '{0[a]:>015},{0[b][1]}'.format(dic)
print 
print "\t'{0:.2f}'.format(1.3345) 保留2位小数 =>",'{0:.2f}'.format(1.3345)
print "\t'{0:10.2f}'.format(1.3345) =>",'{0:10.2f}'.format(1.3345)
print "\t'{0:010.2f}'.format(1.3345) 不够10位补0 =>",'{0:010.2f}'.format(1.3345)
print "\t'{0:<010.2f}'.format(1.3345) 向左对齐，不够10位补0 =>",'{0:<010.2f}'.format(1.3345)
print "\t'{0:>10.2f}'.format(1.3345)  向右对齐 =>",'{0:>10.2f}'.format(1.3345)
print "\t'{0:^010.2f}'.format(1.3345) 居中对齐 =>",'{0:^10.2f}'.format(1.3345)                 
print
print "\t'{0.platform}'.format(sys) => "   ,   '{0.platform}'.format(sys)
