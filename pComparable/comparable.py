#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File: comparable.py
Description: This file defines the class queue
Author: Larry Yu
Initial Data: Nov 25th, 2018
"""

class Comparable(object):
    """
    Wrapper class for items that are not comparable
    """

    def __init__(self, data, priority = 1):
        self._data = data
        self._priority = priority

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        """
        To check if other has the same priority with self
        """
        result = False
        if None != other:
            if type(self) == type(other):
                if other is self:
                    result = True
                else:
                    if self._priority == other.priority:
                        result = True
        
        return result

    def getData(self):
        return self._data

    def getPriority(self):
        return self._priority

    def __lt__(self, other):
        if(None != other and type(self) == type(other)):
            return self._priority < other._priority

    def __le__(self, other):
        if(None != other and type(self) == type(other)):
            return self._priority <= other._priority

    def __gt__(self, other):
        if(None != other and type(self) == type(other)):
            return self._priority > other._priority

    def __ge__(self, other):
        if(None != other and type(self) == type(other)):
            return self._priority >= other._priority             

                

def main():
    pass

if "__main__" == __name__:
    main()