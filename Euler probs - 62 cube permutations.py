# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 19:57:24 2015

@author: JKandFletch
"""


def getDigits(num):
    numStr = str(num)
    result = [0]*10
    
    for val in numStr:
        result[int(val)] += 1
    
    return tuple(result)

results = {}
thisSet = 0
n = 1

while thisSet < 5:
    thisVal = n**3
    digits = getDigits(thisVal)
    try:
        results[digits].append(thisVal)
        thisSet = len(results[digits])
    except:
        results[digits] = [thisVal]
        thisSet = 1
    n += 1

print digits
print results[digits]