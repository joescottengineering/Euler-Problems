# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:01:43 2015

@author: JKandFletch
"""
numbers = []

for n in range(2,999999):
    total = 0
    for digit in str(n):
        total += int(digit)**5
    if total == n:
        numbers.append(n)

print numbers
print sum(numbers)