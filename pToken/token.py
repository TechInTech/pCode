#!/usr/bin/python3
#!-*- coding:utf-8 -*-
"""
File: token.py
Description: This file defines the class token.
Author: Larry Yu
Initial date: Nov 12th, 2018
"""

class Token(object):
    
    #Type code definition
    UNKNOWN = 0
    INT = 4
    MINUS = 5
    PLUS = 6
    MUL = 7
    DIV = 8
    FIRST_OP = 5
    
    def __init__(self, value):
        if int == type(value):
            self._type = Token.INT
        else:
            self._type = self.makeType(value)
        self._value = value
    
    def makeType(ch):
        result = None
        if "*" == ch:
            result = Token.MUL
        elif "/" == ch:
            result = Token.DIV
        elif "+" == ch:
            result = Token.PLUS
        elif "-" == ch:
            result = Token.MINUS
        else:
            result = Token.UNKNOWN

        return result

    def getValue(self):
        return self._value

    def getType(self):
        return self._type

    def __str__(self):
        return str(self._value)

    def isOperator(self):
        return self._type >= Token.FIRST_OP

def test():
    pass

if "__main__" == __name__:
    test()