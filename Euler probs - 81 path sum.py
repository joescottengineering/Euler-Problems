# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:49:43 2015

@author: JKandFletch
"""


class Node(object):

    def __init__(self, name, value):
        self.rightNode = None
        self.downNode = None
        self.parentNode = None
        self.nodeName = name
        self.value = value
        self.minSum = value

    def setParent(self, node):
        self.parentNode = node

    def setRight(self, node):
        self.rightNode = node

    def setDown(self, node):
        self.downNode = node

    def setValue(self, num):
        self.value = num

    def setMinSum(self, num):
        self.minSum = self.value + num

    def getParent(self):
        return self.parentNode

    def getRight(self):
        return self.rightNode

    def getDown(self):
        return self.downNode

    def getValue(self):
        return self.value

    def getMinSum(self):
        return self.minSum

    def getName(self):
        return self.nodeName

    def hasRight(self):
        if self.rightNode is None:
            return False
        else:
            return True

    def hasDown(self):
        if self.downNode is None:
            return False
        else:
            return True


node_dict = {}
file_path = 'C:/Users/JKandFletch/Documents/Joe Play/Code/Euler/Euler probs - 81 matrix.txt'
row_num = 0

with open(file_path, 'r') as matrix_in:
        for line in matrix_in.readlines():
#            print line
            #currentLine = line.rstrip()
            current_row = line.split(',')
            line_len = len(current_row)
            for n, val in enumerate(current_row):
                pos = (n, row_num)
                node_dict[pos] = Node(pos, int(val))
                if n < (line_len - 1):
                    node_dict[pos].setRight((n + 1, row_num))
                if row_num < (line_len - 1):
                    node_dict[pos].setDown((n, row_num - 1))
            row_num += 1

#for key in node_dict.keys():
#    print node_dict[key].getValue()

for x in range(row_num - 1, -1, -1):
    for y in range(row_num - 1, -1, -1):
        this_node = (x, y)
        right_node = node_dict[this_node].getRight()
        down_node = node_dict[this_node].getDown()
        if right_node is None:
            if down_node is None:
                min_path = 0
            else:
                min_path = node_dict[(x, y + 1)].getMinSum()
        else:
            if down_node is None:
                min_path = node_dict[(x + 1, y)].getMinSum()
            else:
                min_path = min((node_dict[(x + 1, y)].getMinSum(),
                                node_dict[(x, y + 1)].getMinSum()))
        node_dict[this_node].setMinSum(min_path)

print node_dict[(0,0)].getMinSum()
