#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: linkedlist.py
Description: This file defines the class linkedlist
Author: Larry Yu
Initial Date: Dec 3rd, 2018
"""

import sys
sys.path.append("/mnt/d/repo/pCode")
from pAbstractlist.abstractlist import AbstractList
from pTwoWayNode.twoWayNode import TwoWayNode

class LinkedList(AbstractList):
    """
    To represent the class linkedlist which is implemented based on AbstractList
    """
    def __init__(self, sourceCollection = None):
        #This is the sentinal node
        self._head = TwoWayNode(None)
        self._head.setNext(self._head)
        self._head.setPrevious(self._head)
        AbstractList.__init__(self, sourceCollection)

    def __iter__(self):
        cursor = self._head.getNext()
        while(cursor != self._head):
            yield cursor.getValue()
            cursor = cursor.getNext()

    def __getItem__(self, i):
        """To get the item at position i"""
        #Precondition: 0 <= i < len(self)
        #PostCondition: Return the item at position i
        cursor = 0
        tempNode = self._head.getNext()
        if(i in range(0, len(self))):
            while(cursor < i):
                tempNode = tempNode.getNext()
                cursor += 1 

            return tempNode.getValue()
        else:
            raise IndexError("Index out of range.")

    def __setItem__(self, i, value):
        """To set the value at postion i to the given value"""
        #Precondition 0 <= i < len(self)
        #PostCondition The value at position i is set to the given value
        cursor = 0
        tempNode = self._head.getNext()
        if(i in range(0, len(self))):
            while(cursor < i):
                tempNode = tempNode.getNext()
                cursor += 1 

            tempNode.setValue(value)
        else:
            raise IndexError("Index out of range.")


    def insert(self, i, value):
        """Insert one node at """
        pass

#For test purpose
def main():
    pass

if "__main__" == __name__:
    main()