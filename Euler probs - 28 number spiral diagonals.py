# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 19:21:40 2015

@author: JKandFletch
"""

squareSize = 1001


total = 1
nextStep = 1
n = 2

while n <= squareSize:
    for i in range(1, 5):
        nextStep = nextStep + n
        total += nextStep
        print nextStep
    n += 2


print total
