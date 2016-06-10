#!/usr/bin/python
# -*- coding:utf-8 -*-


'''

movie = ["The Holy Grail","The Life of Brian","The Meaning of Life"]


movie.insert(movie.index('The Holy Grail')+1,1975)
movie.insert(movie.index('The Life of Brian')+1,1979)
movie.insert(movie.index('The Meaning of Life')+1,1983)


print movie

for i in movie:
    print i

'''


movies = ['The Holy Grail', 1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print nested_item
    else:
        print each_item
