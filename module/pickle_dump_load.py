#!/usr/bin/python
# -*- coding:utf-8 -*-



import pickle

name = 'python'

dic = dict.fromkeys(['a','b'],100)

game = dict(zip(dic.keys(),dic.values()))

pickle.dump([game,name,dic],open('pickle_dump_load.dat','wb'))

db = pickle.load(open('pickle_dump_load.dat','rb'))

print db


