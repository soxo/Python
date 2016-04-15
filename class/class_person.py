#!/usr/bin/python
# -*- coding:utf-8 -*-


# Script Name   : class_person.py
# Author        : Zhang Dong  
# Last Modified :  
# Version       : 1.0 
# Last Modified : 



class Person:
	population = 0

	def __init__(self,name):
		self.name = name
		Person.population += 1

	def sayHello(self):
		Person.population += 1
		print "Therea re still %d people left." % Person.population

	

p = Person()
p.sayHello()
