#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File:stack.py
Description: This file defines the data structure stack which is implemented by list
Author:Larry Yu
Initial Data: Dec 23rd, 2018
"""
class Stack(object):
    """
    To represent the class Stack
    """
    def __init__(self):
        self._size = 0
        self._container = list()

    def isEmpty(self):
        return 0 == self._size

    def push(self, data):
        self._container.append(data)

    def __len__(self):
        return self._size

    def pop(self):
        #Precondition: The stack is not empty
        #Postcondition: The item at the top is poped
        item = None
        if not self.isEmpty():
            item = self._container[-1]

        return item

#For test purpose
def main():
    pass


if "__main__" == __name__:
    main()