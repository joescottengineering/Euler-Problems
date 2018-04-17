# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 20:15:01 2015

@author: JKandFletch
"""

import itertools

testList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(itertools.permutations(testList))

for i in range(20):
    print result[i]
