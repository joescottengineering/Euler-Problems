# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 21:58:28 2015

@author: JKandFletch
"""

number = 2**1000
result = 0

for c in str(number):
    result += int(c)
    
print result