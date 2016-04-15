#!/usr/bin/python
# -*- coding -*- 




# Script Name   : sys_argv.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  



import sys
'''
print sys.argv
scriptName,first,second = sys.argv
print 'THe script name: %s' % sys.argv[0] 
print 'THe script name: %s' % scriptName
print 'The first: %s' % first

'''


def argv_two(*argvs):
    scriptName,fileName = sys.argv
    a,b = argvs
    print scriptName,fileName
    print a,b


argv_two('hello','world')
    

    
