#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: abstractCollection.py
Description: This file defines the class abstractcollection
Author: Larry Yu
Initial Date: Dec 3rd, 2018
"""

import sys
sys.path.append("/mnt/d/repo/pCode")
from pAbstractCollection.abstractCollection import AbstractCollection

class AbstractList(AbstractCollection):
    def __init__(self, sourceCollection):
        AbstractCollection.__init__(self, sourceCollection)
        self._modCount = 0

    def getModCount(self):
        return self._modCount
    
    def increModCount(self):
        self._modCount += 1
    
    def index(self, item):
        """
        return the position of given content
        """
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position += 1
        if position == len(self):
            raise ValueError(str(item) + "not in list")
    
    def add(self, item):
        self.insert(len(self), item)

    def remove(self, item):
        position = self.index(item)
        self.pop(position)


def main():
    tempList = []
    lst = AbstractList(tempList)

if "__main__" == __name__:
    main()