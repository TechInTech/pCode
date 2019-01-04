"""
File: hashtable.py
Description: This file implements the class HashSet and some test functions as auxliary
Author: Larry Yu
Initiated Data: Jan 2nd, 2019
"""

from pNode.node import Node
from pArray.arrays import Array
from pAbstractDict.abastractDict import AbstractDict, Item

class HashSet(object):
    """
    A hashing implementation of a set
    """

    DEFAULT_CAPACITY = 3

    def __init__(self, sourceDirectory = None):
        """
        Will copy items to collection from sourceDirectory if it's present
        """
        self._array = Array(HashSet.DEFAULT_CAPACITY)
        self._foundNode = self._priorNode = None
        self._index = -1
        self._size = 0
        AbstractDict.__init__(self, sourceDirectory)

    #Accesor
    def __contains__(self, key):
        """
        Return True if key exists in self or False otherwise
        """
        self._index = abs(hash(key)) % len(self._array)
        self._priorNode = None
        self._foundNode = self._array[self._index]
        while None != self._foundNode:
            if key == self._foundNode.data.key:
                return True
            else:
                self._priorNode = self._foundNode
                self._foundNode = self._foundNode.next

        return False

    def __iter__(self):
        for item in self._array:
            if None != item:
                yield item.data.value
                item = item.next
    
    def __getitem__(self, key):
        if key in self:
            return self._foundNode.data.value
        else:
            raise IndexError("The given key is not in the dictionary")

    #Mutators
    def __setitem__(self, key, value):
        """
        If the key exists in dictionary, replace the old value with the given value.
        Otherwise, create new key and set its value.
        """
        if key in self:
            self._foundNode.data.value = value
        else:
            newNode = Node(Item(key, value), self._array[self._index])
            self._array[self._index] = newNode
            self._size += 1

    def pop(self, key):
        #We should always run "__contains__" in the fisrt place
        if not key in self:
            raise IndexError("The given key does not exist in the dictionary.")
        #The first node in the linked list is the node we are looking for
        elif(None == self._priorNode):
            self._array[self._index] = self._foundNode.next
        else:
            self._priorNode = self._foundNode.next
            
        self._size -= 1

        return self._foundNode.data.value

#For test purpose
def main():
    pass

if "__main__" == __name__:
    main()