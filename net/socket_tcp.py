#!/usr/bin/python
# -*- coding:utf-8 -*-




import time,socket


host =""
port = 12306
addr = (host,port)

socktcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socktcp.bind(addr)
socktcp.listen(5)
conn,address = socktcp.accept()

print 'Waiting......'
while True:
    data = conn.recv(1024)
    print data
    if not data:
        break
    conn.sendall(data)

conn.close()
    




    





