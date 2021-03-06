#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File: queue.py
Description: This file defines the class queue
Author: Larry Yu
Initial Date: 18th Nov, 2018
"""
import sys
sys.path.append("/cygdrive/d/pCode/")
from pNode.node import Node
import random

class Queue(object):
    """
    To represent the class Queue
    """
    def __init__(self):
        self._head = None
        self._rear = None
        self._size = 0
        
    def enQueue(self, value):
        if self.isEmpty():
            self._head = Node(value, None)
            self._rear = self._head
        else:
            self._rear.setNext(Node(value, None))
            self._rear = self._rear.getNext()
        self._size += 1

    def deQueue(self):
        if(self._size > 0):
            retValue = self._head.getData()
            if(self._head == self._rear):
                self._head = None
                self._rear = None
            else:
                self._head = self._head.getNext()
            self._size -= 1
            return retValue
        else:
            raise AttributeError("Qeueu is empty!")
    
    def __len__(self):
        return self._size

    def __iter__(self):
        tempList = list()
        tempNode = self._head
        while(tempNode):
            tempList.append(tempNode.getData())
            tempNode = tempNode.getNext()
        return iter(tempList)

    def __str__(self):
        retStr = ""
        tempNode = self._head
        while(tempNode):
            retStr += str(tempNode.getData()) + " "
            tempNode = tempNode.getNext()
        return retStr.strip()
        
    def peek(self):
        if(len(self) > 0 and self._head != None):
            return self._head.getData()
        else:
            raise AttributeError("Qeueu is empty!")

    def isEmpty(self):
        return 0 == self._size

    def __eq__(self, other):
        if None != other:
            if other is self:
                return True
            if type(other) != type(other) or len(self) != len(other):
                return False
            for item in other:
                if not item in self:
                    return False
            return True
        else:
            return False

class PriorityQueue(Queue):
    """
    This class is sub class of Queue. This class implements the priority class.
    """

    def __init__(self):
        Queue.__init__(self)

    def enQueue(self, data):
        if self.isEmpty() or data >= self._rear.getData():
            Queue.enQueue(self, data)
        else:
            #Search for a proper position for new node
            probe = self._head
            while(data >= probe.getData()):
                trailer = probe
                probe = probe.getNext()
            
            newNode = Node(data, probe)
            
            if probe == self._head:
                self._head = newNode
            else:
                trailer.setNext(newNode)
        self._size += 1
            

def main():
    pq = PriorityQueue()
    for _ in range(10):
        pq.enQueue(random.randint(1, 100))
    #print(q)

    for item in pq:
        print(item)

if "__main__" == __name__:
    main()