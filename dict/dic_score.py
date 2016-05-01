#!/usr/bin/python
# -*- coding:utf-8 -*-



score = {
    'zhangsan':98,
    'yangming':67,
    'chenhong':89,
    'liuming':96,
    'wangsanhong':54,
    'huazhi':0
}

db = []
for i in score:
    db.append((score[i],i))

for x,y in sorted(db,reverse=True):
     print y,x

print '*' * 40

print sorted([(n,m) for m,n in score.iteritems()],reverse=True)

