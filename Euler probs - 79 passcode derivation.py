# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:09:09 2015

@author: JKandFletch
"""


def getFirsts(str_list):
    firsts = ''
    nots = ''
    for value in str_list:
        val_len = len(value)
        if val_len == 0:
            continue
        elif val_len == 1:
            firsts += value
        else:
            firsts += value[0]
            nots += value[1:]
    only_firsts = ''
    for first in firsts:
        if (first not in nots) and (first not in only_firsts):
            only_firsts += first
    return list(only_firsts)


def getMaxLen(str_list):
    max_len = 0
    for item in str_list:
        if len(item) > max_len:
            max_len = len(item)
    return max_len

def stripValues(char, str_list):
    new_list = []
    for item in str_list:
        new_str = item.strip(char)
        new_list.append(new_str)
    return new_list

file_path = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Euler/Eulerprobs'\
                ' - 79 keylogs.txt'

values = []

with open(file_path, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        if line not in values:
            values.append(line)

guess = ''

while getMaxLen(values) > 0:
    next_first = getFirsts(values)
    guess += next_first[0]
    values = stripValues(next_first[0], values)

print guess
