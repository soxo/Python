#!/usr/bin/python
# -*- coding:utf-8 -*-


__metalclass__ = type


class Book:
    name = 'Study python.'
    @staticmethod
    def read():
        page = 450
        print "Reading %s" % Book.name

class Text_Book:
    @classmethod
    def sell(cls):
        amount = 10000
        print "sell: %d" % amount

if __name__ == "__main__":

    java = Book()
    java.read()
    Book.read()

    php = Text_Book()
    php.sell()
    Text_Book.sell()
