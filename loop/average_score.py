#!/usr/bin/python
# -*- coding:utf-8 -*-



#输入一串成绩分数，统计平均分数，按-1退出


counter = 0
total = 0
score = 0
while score != -1:
    try:
        score = int(raw_input("Enter score, -1 to End: "))
        if score != -1:
            total = total + score
            counter = counter + 1
    except:
        print "Please enter a number."

if counter != 0:
    average = float(total)/counter 
    print 'Average: %s' % average
else:
    print "No grade were entered"


    



print '*' * 40

db = []
while True:
    score = raw_input("Enter score, -1 to End: ")
    if score != '-1' and score.isdigit():
        db.append(int(score))
    elif score == '-1':
        break
    else:
        print "Please enter a number."

if db != []:
    average = float(sum(db))/len(db)
    print 'Average: %s' % average
else:
    print "No grade were entered"








