# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 21:54:52 2015

@author: JKandFletch
"""


maxSum = 0

for a in range(100):
    for b in range(100):
        tempNum = a**b
        tempStr = str(tempNum)
        thisSum = 0

        for char in tempStr:
            thisSum += int(char)

        if thisSum > maxSum:
            maxSum = thisSum
            print a, b, tempNum

print maxSum
