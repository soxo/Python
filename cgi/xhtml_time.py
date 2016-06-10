#!/usr/bin/python
# -*- coding:utf-8 -*-


import time

def print_html(title):
    print """Content-type:text/html

<?xml version = "1.0" encoding = "UTF-8"?>
<!DOCTYPE html PUBLIC
    "-//W3C//DTD XHTML 1.0 Strict//EN"
    "DTD/xhtml1-strict.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head><title>%s</title></head>

<body>""" % title


print_html("Current date and time")
print time.ctime(time.time())
print "</body></html>"
