# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 21:25:21 2015

@author: JKandFletch
"""


def getValue(string):
    values = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    num_chars = len(string)
    this_total = 0
    for n, char in enumerate(string):
        this_val = values[char] 
        if n < (num_chars - 1):
            if this_val < values[string[n + 1]]:
                this_val *= -1
        this_total += this_val
    return this_total


def calcValue(num):
    num_values = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), 
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), 
                  (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    index = 0
    remaining = num
    result = ''
    while remaining > 0:
        this_value = num_values[index][0]
        num_times = remaining/this_value
        if num_times == 0:
            index += 1
            continue
        else:
            result += num_times * num_values[index][1]
        remaining -= num_times * this_value
        index += 1
    return result

file_path = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Euler/\
Euler probs - 89 roman numerals.txt'

orig_len = 0
new_len = 0

with open(file_path, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        orig_len += len(line)
        this_num = getValue(line)
        best_chars = calcValue(this_num)
        new_len += len(best_chars)

print orig_len, new_len
print orig_len - new_len
