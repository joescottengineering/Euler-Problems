# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 21:19:39 2015

@author: JKandFletch
"""
import math

total = 0

result = str(math.factorial(100))

for char in result:
    total += int(char)

print total