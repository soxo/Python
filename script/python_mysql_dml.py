#!/usr/bin/python
# -*- coding:utf-8 -*-



# Script Name   : python_mysql_dml.py 
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 



import MySQLdb


conn = MySQLdb.connect(host='localhost',user='root',passwd='      ')
cur = conn.cursor()
cur.execute('create database  if not exists python')
cur.select _db('use python')
cur.execute('select  database()')
print cur.fetchall()

