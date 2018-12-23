#!/usr/bin/python3
#-*-coding:utf-8-*-
"""
File: arraylistiterator.py
Description: This file defines the class ArrayListIterator
Author: Larry Yu
Initial Date: Dec 8th, 2018
"""

import sys
sys.path.append("/mnt/d/repo/pCode/")
from pAbstractCollection.abstractCollection import AbstractCollection
from pBsNode.bstnode import BSTNode
from pStack.stack import Stack

class LinkedBST(AbstractCollection):
    """
    To represent the class LinkedBST
    """
    def __init__(self, sourceCollection):
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    def find(self, item):
        """
        To find specific item in BST
        """
        def recurse(node):
            """
            The node is the root node of the tree in which you want to find the give item
            """
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

            return recurse(self._root)

    def inorder(self):
        lyst = list()
        def recurse(node):
            if None != node:
                recurse(node.left)
                lyst.append(node)
                recurse(node.right)

        recurse(self._root)
        return iter(lyst)

    def preorder(self):
        lyst = list()
        def recurse(node):
            if None != node:
                lyst.append(node)
                recurse(node.left)
                recurse(node.right)
        recurse(self._root)
        return iter(lyst)

    def postOrder(self):
        lyst = list()
        def recurse(node):
            if None != node:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node)
        recurse(self._root)
        return iter(lyst)


    def __str__(self):
        """
        To display the whole tree which is turned 90 degress anti-clockwise
        """

        def recurse(node, level):
            s = ""
            if None != node:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += node.data
                s += recurse(node.left, level + 1)
            
            return recurse(self._root, 0)

    def add(self, data):
        """
        To add data into the proper position of current tree
        """

        def recurse(node):
            if data < node.data:
                if None == node.left:
                    node.left = BSTNode(data)
                else:
                    recurse(node.left)
            #If data is greater or equal to current node
            elif None == node.right:
                node.right = BSTNode(data)
            else:
                recurse(node.right)
            #The end of recurse

        if self.isEmpty():
            self._root = BSTNode(data)
        else:
            recurse(self._root)
        self._size += 1

    def __contains__(self, data):
        """
        To judge if the given data exist in current tree.
        """
        lyst = list()
        def recurse(node):
            if None != node:
                recurse(node.left)
                lyst.append(node.data)
                recurse(node.right)

        recurse(self._root)
        return data in lyst

    def remove(self, data):
        #Precondition: The given data is in the tree.
        #Postcondition: The node is removed form tree, and the tree is still BST after removing.
        if None != self._root and data in self:
            #Need to find this node in current tree
            pass

    def preOrderWithStack(self):
        s = Stack()
        if len(self) != 0:
            s.push(self._root)
        while(not s.isEmpty()):
            item = s.pop()
            yield item
            if None != item.right:
                s.push(item.right)
            if None != item.left:
                s.push(item.left)


def main():
    pass

if "__main__" == __name__:
    main()