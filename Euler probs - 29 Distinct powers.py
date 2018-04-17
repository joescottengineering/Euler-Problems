# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 21:07:06 2015

@author: JKandFletch
"""

sequence = []

for a in range(2,101):
    for b in range(2,101):
        term = a**b
        if term in sequence:
            continue
        else:
            sequence.append(term)
            
print len(sequence)