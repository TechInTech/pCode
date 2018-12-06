#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: twoWayNode.py
Description: This file defines the class twoWayNode
Author: Larry Yu
Initial Date: Dec 3rd, 2018
"""

class TwoWayNode(object):
    """
    To represent the class TwoWayNode
    """
    def __init__(self, value):
        self._value = value
        self._next = None
        self._previous = None

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def getPrevious(self):
        return self._previous

    def setNext(self, next):
        self._next = next

    def setPrevious(self, previous):
        self._previous = previous

    def setValue(self, value):
        self._value = value

#For test purpose
def main():
    pass

if "__main__" == __name__:
    main()