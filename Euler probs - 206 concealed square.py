# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:22:35 2015

@author: JKandFletch
"""

import math


def check_result(n):
    check = '1234567890'
    value = str(n)
    val_check = ''
    for i in range(len(value)):
        if i % 2 == 0:
            val_check += value[i]
    if val_check == check:
        print 'FOUND'
        return True
    else:
        return False

n = int(math.sqrt(19293949596979899))*10
found = False

while not found:
    n -= 10
    try_this = n**2
    found = check_result(try_this)

print n, try_this
