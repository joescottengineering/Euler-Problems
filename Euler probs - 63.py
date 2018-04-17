# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:32:19 2015

@author: JKandFletch
"""


maxValue = 10
n = 1
limit = str(9**1)
results = []

while len(limit) == n:
    for i in range(1, 10):
        value = i**n
        if len(str(value)) == n:
            results.append([i, n, value])
    n += 1
    limit = str(9**n)

print results
print len(results)
