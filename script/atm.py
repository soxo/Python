#!/usr/bin/python
#_*_ coding:utf-8 _*_

# Script Name   : atm.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified :  
 
  


import sys,datetime,os
accountPassword = {'342543134221212498':'345623','532212298712347687':'123456','876234789098223437':'876232','324256789212345678':'125324'}

def cardPassword():
    '''此函数作用:验证用户名和密码'''

    loginTime = datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    account = raw_input('account: ').strip()
    with open('user_name.lock','a+') as f:
        for line in f:
            if account in line:
                print "account has been locked!"
                sys.exit()
            else:
                pass

    for i in range(3):
        password = raw_input('Password: ').strip()
        if  accountPassword.get(account) == password: 
            print "Welcome ,%s ,Login Successi!" % loginTime
            break
        elif not password:  #判断按回车密码为空时，继续提示输入密码
            continue
        else:
            print  "Password error,please re-enter!"
    else:
        with open('UserName.lock','a+') as f:
            f.write('%s, %s has been Locked!' %(loginTime,account))
        print 'Enter too many times, the account is locked!'
        sys.exit()

cardPassword()
print cardPassword.__doc__    #打印开头文档说明


'''
def cardPassword(account,Password):
    if (len(account) == 18) and (account in accountPassword ) and (accountPassword[account] == Password):
        print "Welcome ,%s ,Login Successi!" % datetime.datetime.now().strftime('%Y%m%d %H:%M:%S')
    else:
        for i in range(3):
            
        print "Login Failed"     
cardPassword(sys.argv[1],sys.argv[2])

'''


