#!/usr/bin/python
# -*- coding:utf-8 -*-




import random

db = []

for i in range(1,600000):
    db.append(random.randrange(1,7))
print '''\
1: {} times
2: {} times
3: {} times
4: {} times
5: {} times
6: {} times'''.format(db.count(1),db.count(2),db.count(3),db.count(4),db.count(5),db.count(6)) 

print '*' * 40


def play_point():
    point = random.randrange(1,7) + random.randrange(1,7)
    print 'point: %d' % point
    if point == 7:
        print 'Point %15d: You lose' % point
    elif point in [4,5,6,8,9,10]:
        print 'Point %15d: You win' % point
    else:
        while True:
            point = random.randrange(1,7) + random.randrange(1,7)
            print 'second point: %d' % point
            if point in [4,5,6,8,9,10]:
                print 'Point %15d: You win' % point
                break
            


def play():
    total = random.randrange(1,7) + random.randrange(1,7)
    print 'total: %d' % total 
    if total in [7,11]:
        print '%15d: You win' % total
    elif total in [2,3,12]:
        print '%15d: You lose' % total
    else:
        play_point()


play()
                    

            






        
