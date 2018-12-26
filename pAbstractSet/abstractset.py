#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File: abstructset.py
Description: This file defines the class "AbstructSet" interface
Author: Larry Yu
Initial Data: Dev 26th, 2018
"""
class AbstructSet(object):
    """Generic set method implementation"""

    def __or__(self, other):
        if type(self) == type(other):
            return self + other
        else:
            raise AttributeError("Worng data type.")
    
    def __and__(self, other):
        if type(self) == type(other):
            interSection = type(self)()
            for item in self:
                if item in other:
                    interSection.add(item)
            return interSection
        else:
            raise AttributeError("Worng data type.")

    def __sub__(self, other):
        if type(self) == type(other):
            difference = type(self)()
            for item in self:
                if item not in other:
                    difference.add(item)
            return difference
        else:
            raise AttributeError("Worng data type.")

    def isSubSet(self, other):
        retValue = False
        if type(self) == type(other):
            for item in self:
                if not item in other:
                    return False
            
            retValue = True

            return retValue
        else:
            raise AttributeError("Worng data type.")

    def __iter__(self):
        pass

#For test purpose
def main():
    pass

if "__main__" == __name__:
    main()