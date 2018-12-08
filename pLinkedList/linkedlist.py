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
        tempNode = self._getItem(i)
        if(None != tempNode):
            return tempNode.getValue()

    def __setItem__(self, i, value):
        """To set the value at postion i to the given value"""
        #Precondition 0 <= i < len(self)
        #PostCondition The value at position i is set to the given value
        tempNode = self._getItem(i)
        if(None != tempNode):
            tempNode.setValue(value)

    def _getItem(self, i):
        """This function returns the two way node at position i"""
        #Precondition: 0 <= i < len(self), or a IndexError will be raised
        #Postcondition: returns the item at postion i
        cursor = 0
        tempNode = self._head.getNext()
        if(i in range(0, len(self))):
            while(cursor < i):
                tempNode = tempNode.getNext()
                cursor += 1 

            return tempNode
        else:
            raise IndexError("Index out of range.")


    def insert(self, i, value):
        """Insert one node at position i"""
        nodeToInsert = TwoWayNode(value)
        if i <= 0:
            nodeToInsert.setNext(self._head.getNext())
            nodeToInsert.setPrevious(self._head.getPrevious())
            self._head.setNext(nodeToInsert)
        elif i > len(self):
            i = len(self)
            self._head.getPrevious().setNext(nodeToInsert)
            self._head.setPrevious(nodeToInsert)
        else:
            tempNode = self._getItem(i)
            tempNode.setPrevious(nodeToInsert)
            nodeToInsert.setNext(tempNode)
            nodeToInsert.setPrevious(tempNode.getPrevious())

        self._size += 1
        self.increModCount()

    def pop(self, i):
        """Return the item at position i and remove it from the list"""
        if i in range(0, len(self)):
            retValue = None
            #Pop the first node
            if 0 == i:
                retValue = self._head.getNext().getValue()
                self._head.setNext(self._head.getNext().getNext())
            #Pop the last node
            elif i == len(self) - 1:
                retValue = self._head.getPrevious().getValue()
                self._head.setPrevious(self._head.getPrevious().getPrevious())
            else:
                tempNode = self._getItem(i)
                retValue = tempNode.getValue()
                tempNode.getPrevious().setNext(tempNode.getNext())
            
            self._size -= 1
            self.increModCount()

            return retValue

        else:
            raise IndexError("Index out of range.")

#For test purpose
def main():
    pass

if "__main__" == __name__:
    main()