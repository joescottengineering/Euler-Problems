# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 20:02:36 2015



@author: JKandFletch
"""

m = 0
n = 0
k = 0
A = 0
B = 0
C = 0

tripSum = 0

for m in range(1000):
    for n in range(1,m):
        k = 1
        
        A = m ** 2 - n ** 2
        B = 2 * m * n
        C = m ** 2 + n ** 2
        
        tripSum = A + B + C
        
        while tripSum < 1000:
            tripSum += tripSum
            k += 1
        if tripSum == 1000:
            print A*B*C
        