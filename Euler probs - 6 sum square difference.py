# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:55:09 2015

@author: JKandFletch
"""

sumofSquares = 0

squareofSum = 0

for i in range(1,101):
    sumofSquares += i**2
    squareofSum += i

squareofSum = squareofSum ** 2

print squareofSum - sumofSquares
