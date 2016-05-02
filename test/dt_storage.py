#!/usr/bin/python
# -*- coding:utf-8 -*-



storage ={}
storage['first'] = {}
storage['middle'] ={}
storage['last'] = {}


me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]


my_sister = 'Anne Lie Heland'
storage['first'].setdefault('Anne',[]).append(my_sister)

print storage

