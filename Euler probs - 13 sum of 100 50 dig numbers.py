# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 22:07:13 2015

@author: JKandFletch
"""

result = sumVar = 0

fileName = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Euler probs - 13 sum of 100 50 dig numbers.txt'

inFile = open(fileName,'r', 0)

for line in inFile:
    sumVar+= int(line)
        
result = str(sumVar)

print result[:10]