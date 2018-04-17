# -*- coding: utf-8 -*-
"""
Euler problem 1 - sum of multiples of 3 or 5 below 1000
"""
result = []


for i in range(1000):
    if i%3 == 0 or i%5 ==0:
        result.append(i)
        
print (sum(result))