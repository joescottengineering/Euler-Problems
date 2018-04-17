# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 15:46:31 2015

@author: JKandFletch
"""

import itertools


def stitches(tupe):
    result = ''
    for i in tupe:
        result += str(i)
    return int(result)


testList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(itertools.permutations(testList))
primes = [2, 3, 5, 7, 11, 13, 17]
thisNum = 0
matches = []

for number in result:
    mightMatch = True
    if number[0] == 0:
        continue
    for i in range(1, 8):
        thisNum = stitches(number[i:i+3])
        if thisNum % primes[i-1] == 0:
            continue
        else:
            mightMatch = False
            break
    if mightMatch:
        matches.append(stitches(number))

print matches
