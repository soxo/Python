#!/usr/bin/python
# -*- coding:utf-8 -*-


width = input('Please enter width: ')
price_width = 10
item_width = width - price_width
heard_format='%-*s%*s'
product_format = '%-*s%*.2f'
print '=' * width
print heard_format  % (item_width,'Item',price_width,'Price')
print '-' * width
print product_format % (item_width,'Apples',price_width,0.24)
print product_format % (item_width,'Pears',price_width,0.50)
print product_format % (item_width,'Cantaloupes',price_width,1.92)


