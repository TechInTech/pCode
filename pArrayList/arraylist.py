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

    def __getitem__(self, i):
        """To get the item at position i,
        precondition: 0 <= i < len(self),
        or IndexError will be raised."""
        if i in range(0, len(self)):
            return self._item[i]
        else:
            raise IndexError("List Index out of range.")

    def __setItem__(self, i, value):
        """To set the item at position i to the given value,
        Precondition: 0 <= i < len(self), or IndexError will
        be raised."""
        if i in range(0, len(self)):
            self._item[i] = value
        else:
            raise IndexError("List Index out of range.")

    def insert(self, i, item):
        """To insert item at position i"""
        #Precondition: Resize array here if necessary
        if i < 0:
            i = 0
        elif i > len(self):
            i = len(self)
        if i in range(0, len(self)):
            for j in range(len(self), i, -1):
                self._item[j] = self._item[j - 1]
        self._item[i] = item
        self._size += 1
        self._modCount += 1

    def pop(self, i = None):
        """To remove and return the element at i"""
        #If i is None, then pop the last element in list.
        if i == None:
            i = len(self)
        elif i not in range(0, len(self)):
            raise IndexError("List index out of range.")
        
        temp = self._item[i]
        for j in range(i, len(self) - 1):
            self._item[j] = self._item[j + 1]

        return temp

    def listItrator(self):
        return ArrayListIterator(self)
    
    
def main():
    lst = [1,2,3,4,5]
    a = ArrayList(lst)
    
if "__main__" == __name__:
    main()