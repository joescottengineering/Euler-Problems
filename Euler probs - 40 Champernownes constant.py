# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 21:00:40 2015

@author: JKandFletch
"""

import time

startTime = time.time()

result = ''
answer = 1


for i in range(1,100000):
    result = result + str(i)
    
for n in range(6):
    answer = int(result[10**n - 1]) * answer
    
print answer
print time.time() - startTime