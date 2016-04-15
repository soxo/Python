#!/usr/bin/python
# -*- coding:utf-8 -*-



# Script Name   : class_type.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  



class A():
    pass



class B(object):
    pass



class C():
    __metaclass = type



if __name__=='__main__':
    print type(A)
    print type(B)
    print type(C)

    print dir(A)
    print dir(B)
    print dir(C)


