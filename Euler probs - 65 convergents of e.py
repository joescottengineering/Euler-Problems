# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 21:00:07 2015

@author: JKandFletch
"""


sequence = [2]
length = 99

for i in range(1, length/3 + 1):
    sequence.append(1)
    sequence.append(2 * i)
    sequence.append(1)

print sequence
print len(sequence)

num = 1
denom = sequence[-1]
for j in range(len(sequence) - 2, -1, -1):
    new_denom = num
    num = sequence[j] * num + denom
    denom = new_denom

total = 0

for char in str(num):
    total += int(char)

print total