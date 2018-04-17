# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 22:29:39 2015

@author: JKandFletch
"""

import math
import time

start = time.time()

squares = []
results = {}
maxNum = 0
maxPerim = 0

for i in range(1,707):
    squares.append(i**2)

for i in range(1,707):
    for j in range(i, 707):
        k = i**2 + j**2
        if k in squares:
            perimeter = i + j + int(math.sqrt(k))
            if perimeter in results and perimeter <= 1000:
                results[perimeter] += 1
            else:
                results[perimeter] = 1
                
for key in results:
    if results[key] > maxNum:
        maxNum = results[key]
        maxPerim = key

print maxNum, maxPerim
print time.time() - start
