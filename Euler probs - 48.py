# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 22:06:14 2015

@author: JKandFletch
"""

sum = 0
limit = 1000

for i in range(1,limit + 1):
    sum += i**i

print sum
result = str(sum)
print result[-10:]