# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 21:54:00 2015

@author: JKandFletch
"""

limit = 1000000
target = 3.0/7.0
closest_val = 0
min_pair = [0, 0]

for i in range(3, limit+1):
    if (i % 7) == 0:
        continue
    temp = (3 * i) / 7
    ratio = float(temp)/float(i)
#    print temp, i, ratio, min_pair
    if ratio > closest_val:
        closest_val = ratio
        min_pair = [temp, i]

print closest_val, min_pair
