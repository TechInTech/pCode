#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: abstractCollection.py
Description: This file defines the class abstractcollection
Author: Larry Yu
Initial Date: Dec 3rd, 2018
"""

class AbstractCollection(object):
    """
    Represents class abstractionCollection
    """

    def __init__(self, sourceCollection):
        self._size = 0
        for item in sourceCollection:
            self.add(item)

    def isEmpty(self):
        return 0 == self._size    

    def __add__(self, other):
        """
        return a new collection containing the contents of self and other
        """
        #Here, self is given as sourceCollection
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __len__(self):
        return self._size

    def __str__(self):
        return "[" + ", ".join(map(str, self)) + "]"

    def __eq__(self, other):
        if type(other) != type(self) or \
           len(self) != len(other):
                return False
        if self is other:
            return True
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
            
def main():
    lst = ["a"]
    a = AbstractCollection(lst)

if "__main__" == __name__:
    main()