# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:49:43 2015

@author: JKandFletch
"""


class Node(object):

    def __init__(self, name):
        self.rightNode = None
        self.downNode = None
        self.parentNode = None
        self.nodeName = name
        self.nodePaths = 0

    def setParent(self, node):
        self.parentNode = node

    def setRight(self, node):
        self.rightNode = node

    def setDown(self, node):
        self.downNode = node

    def setPaths(self, num):
        self.nodePaths = num

    def getParent(self):
        return self.parentNode

    def getRight(self):
        return self.rightNode

    def getDown(self):
        return self.downNode

    def getPaths(self):
        return self.nodePaths

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


size = 20

node_dict = {}
next_nodes = []
start = (0, 0)
next_move = 'Right'

for x in range(size + 1):
    for y in range(size + 1):
        temp_node = Node((x, y))
        if x < size:
            temp_node.setRight((x + 1, y))
        elif x == size:
            temp_node.setPaths(1)
        if y < size:
            temp_node.setDown((x, y + 1))
        elif y == size and x != size:
            temp_node.setPaths(1)
        node_dict[(x, y)] = temp_node

for x in range(size - 1, -1, -1):
    for y in range(size - 1, -1, -1):
        this_node = (x, y)
        right_node = node_dict[this_node].getRight()
        down_node = node_dict[this_node].getDown()
        paths = node_dict[right_node].getPaths() + node_dict[down_node].getPaths()
        node_dict[this_node].setPaths(paths)

print node_dict[(0,0)].getPaths()
