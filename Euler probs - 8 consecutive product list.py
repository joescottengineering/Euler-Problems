# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 19:20:40 2015

@author: JKandFletch
"""

def ListMult(intlist):
    result = 1
    for num in intlist:
        result *= int(num)
    return result

numbers = []
tempList = []
maxProduct = 0
thisProduct = 0
fileName = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Euler probs - 8 number.txt'

inFile = open(fileName, 'r', 0)

for line in inFile.readline():
    for c in line:
        if len(numbers) < 12:
            numbers.append(int(c))
        elif len(numbers) == 12:
            numbers.append(int(c))
            maxProduct = ListMult(numbers)
        else:
            tempList = numbers[1:]
            tempList.append(c)
            numbers = tempList
            thisProduct = ListMult(numbers)
            if thisProduct > maxProduct:
                maxProduct = thisProduct

print maxProduct