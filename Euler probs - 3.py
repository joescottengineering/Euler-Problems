# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 21:44:44 2015
Euler 3 - largest prime factor for 600851475143
@author: JKandFletch
"""

results = []
number = 600851475143
factor = 2

while number > 1:
    if number % factor == 0:
        results.append(factor)
        number = number/factor
    else:
        factor = factor + 1
        
print max(results)
print results