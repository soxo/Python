#!/usr/bin/python
# -*- coding -*-



import MySQLdb 


conn = MySQLdb.connect(host='localhost',passwd='      ',user='root',db='mysql',port=3306)
cur = conn.cursor()
print cur.execute('select host,user,password from user')
print cur.fetchall()
cur.close()
conn.close()

