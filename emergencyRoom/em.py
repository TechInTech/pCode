#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File: em.py
Description: This file emulates one emergency schedule system in hospital 
Author: Larry Yu
Initial Date: Nov 25th, 2018
"""

class Condition(object):
    
    def __init__(self, rank):
        self._rank = rank

    def __ge__(self, other):
        return self._rank >= other._rank

    def __str__(self):
        retValue = ""
        if 1 == self._rank:
            retValue = "Critical"
        elif 2 == self._rank:
            retValue = "Serious"
        else:
            retValue = "Fair"
        
        return retValue

class Patient(object):

    def __init__(self, name, condiition):
        self._name = name
        self._condiition = condiition
    
    def __ge__(self, other):
        return self._condiition >= other._condiition

    def __str__(self):
        return str(self._name) + " / " + str(self._condiition)


def main():
    pass

if "__main__" == __name__:
    main()