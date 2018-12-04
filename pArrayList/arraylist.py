#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: arraylist.py
Description: This file defines the class array list
Author: Larry Yu
Initial Date: Dec 3rd, 2018
"""

import sys
sys.path.append("/mnt/d/repo/pCode")
from pArray.arrays import Array
from pArray.arraylistiterator import ArrayListIterator
from pAbstractlist.abstractlist import AbstractList


class ArrayList(AbstractList):
    
    #Const
    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection):
        self._item = ArrayList(ArrayList.DEFAULT_CAPACITY)
        AbstractList.__init__(self, sourceCollection = None)
    
    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._item[cursor]
            cursor += 1
    
    
def main():
    pass
    
if "__main__" == __name__:
    main()