#!/usr/bin/python
# -*- coding:utf-8 -*-


__metaclass__ = type


class Person:
    def set_name(self,name):
        self.name = name
        self.tall = 180
    
        
    def print_var(self):
        print self.name
        print self.k
        print self.tall


if __name__ == "__main__":
    zhangdong = Person()
    zhangdong.set_name('zhangdong')
    zhangdong.k = 'admin'
    zhangdong.print_var()
    print zhangdong.name
    print zhangdong.tall

