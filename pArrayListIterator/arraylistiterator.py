#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: arraylistiterator.py
Description: This file defines the class ArrayListIterator
Author: Larry Yu
Initial Date: Dec 8th, 2018
"""

class ArrayListIterator(object):
    """
    To represent the class ArrayListIterator
    """

    def __init__(self, backingStore):
        #Should be the list itself
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        #Move the cursor to the begining of the list
        self.first()

    def first(self):
        self._cursor = 0
        self._lastItemPos = -1

    def hasNext(self):
        return self._cursor < len(self._backingStore)

    def next(self):
        """
        Move the cursor to the next position
        """
        #Precondition: hasNext() returns True, the list has not been modified except by this iterator's mutators.
        #Postcondition: Return the current item and advances the cursor
        if not self.hasNext():
            raise ValueError("No next item in this list iterator")
        
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]

    def last(self):
        """Move the cursor to the ending of the list"""
        self._cursur = len(self._backingStore)
        self._lastItemPos = -1

    def replace(self, value):
        """To replace current item with given value"""
        #Precondition: self.__lastItemPos should not be -1
        #PostCondition: Item at current positon is replaced with given value
        if -1 == self._lastItemPos:
            raise AttributeError("Current position is not defined.")
        
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Link has been modified illegally.")

        self._backingStore[self._lastItemPos] = value
        self._lastItemPos = -1

    def remove(self):
        if -1 == self._lastItemPos:
            raise AttributeError("Current position is not defined.")
        
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Link has been modified illegally.")      

        item2Remove = self._backingStore.pop(self._lastItemPos)

        #If the item removed was obtained via next, move cursor back

    def hasPrevious(self):
        """To judge if current postion has previous node"""
        return 0 < self._cursor

    def previous(self):
        """Move the cursor to the previous position of current node"""
        #Precondition: hasPrevious returns True
        #Postcondition:
        if not self.hasPrevious():
            raise ValueError("No previous item in this list iterator")
        
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("Illegal modification of backing store.")
        self._lastItemPos = self._cursor
        self._cursor -= 1
        return self._backingStore[self._lastItemPos]


#For tesr purpose
def main():
    pass

if "__main__" == __name__:
    main()