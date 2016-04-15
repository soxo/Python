#!/usr/bin/python
# -*- coding -*-


# Script Name   : python_mysql.py 
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 


import MySQLdb 


conn = MySQLdb.connect(host='localhost',passwd='      ',user='root',db='mysql',port=3306)
cur = conn.cursor()
print cur.execute('select host,user,password from user')
print cur.fetchall()
cur.close()
conn.close()

