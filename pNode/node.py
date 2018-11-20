#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
File: node.py
Description: This file defines the class node
Author: Larry Yu
Initial Data: Oct 28th, 2018
"""
import sys
sys.path.append("/cygdrive/d/pCode")

class Node(object):
    def __init__(self, data, next):
        self._data = data
        self._next = next

    def setNext(self, next):
        self._next = next

    def setData(self, data):
        self._data = data

    def getNext(self):
        return self._next

    def getData(self):
        return self._data

def generateLinkedNodeList(size, initialValue = None):
    head = None
    if(size > 0):
        for _ in range(size):
            head = Node(initialValue, head)
    return head

def getLinkedList(head):
    """
    Input: 1. head: the referece to the first node in list
    Output: The list which contains all elements in linked list
    """
    lst = []
    currentNode = head
    while(None != currentNode):
        lst.append(str(currentNode.getData()))
        currentNode = currentNode.getNext()
    return lst

def findElement(lst, itemToFind):
    index = 0
    if(lst and itemToFind):
        currentNode = lst
        while(None != currentNode):
            if(itemToFind == currentNode.getData()):
                return index
            else:
                currentNode = currentNode.getNext()
                index += 1
    return -1

def addNodeIntoList(lst, size, InitialValue = None):
    """
    To add more nodes into designated list
    Input: 1.head: The head of the list
           2.size: How many nodes to add
           3.initialValue: The initial value of nodes
    Output:1. The head of the list
    """
    if(type(int) == type(size) and size >= 0):
        pass

def removeNode(lst, elementToRemove):
    """
    Precondition: The element is in list
    """
    head = lst
    if(None != lst):
        #If the first head is the element to remove
        if(elementToRemove == head.getData()):
            head  = head.getNext()
            return(True, head)
        else:
            currentNode = lst
            while(currentNode.getNext() != None):
                if(currentNode.getNext().getData() == elementToRemove):
                    currentNode.setNext(currentNode.getNext().getNext())
                    return(True, lst)
                currentNode = currentNode.getNext()
    return(False, None)

def test():
    #lst = generateLinkedNodeList(3, 1024)
    #print(getLinkedList(lst))
    #(result, lst) = removeNode(lst, 1024)
    #if(result):
    #    print(getLinkedList(lst))
    #(result, lst) = removeNode(lst, 1024)
    #if(result):
    #    print(getLinkedList(lst))
    #(result, lst) = removeNode(lst, 1024)
    #if(result):
    #    print(getLinkedList(lst))

    head = None
    for index in range(3):
        head = Node(index, head)

    print(getLinkedList(head))
    (result, lst) = removeNode(head, 0)
    if(result):
        print(getLinkedList(lst))   

def main():
    test()

if "__main__" == __name__:
    main()