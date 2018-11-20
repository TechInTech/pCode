#!/usr/bin/python3
#-*- coding:utf-8 -*-

"""
File: node.py
Description: This file 5 sorting algorithms
Author: Larry Yu
Initial Data: Oct 28th, 2018
"""

def swap(targetList, i, j):
    if(i in range(len(targetList)) and j in range(len(targetList))):
        temp = targetList[i]
        targetList[i] = targetList[j]
        targetList[j] = temp

def partition(targetList, left, right):
    middle = (left + right) // 2
    povit = targetList[middle]
    #Swith the povit and right element
    swap(targetList, middle, right)
    boundary = left
    for index in range(left, right):
        if(targetList[index] < povit):
            swap(targetList, index, boundary)
    #switch back boundary and right
    swap(targetList, boundary, right)
    return boundary

def quickSortHelper(targetList, left, right):
    povitLocation = partition(targetList, left, right)
    quickSortHelper(targetList, left, povitLocation)
    quickSortHelper(targetList, povitLocation + 1, right)

def quickSort(targetList):
    if(None != targetList):
        quickSortHelper(targetList, 0, len(targetList) - 1)

def bubbleSort(targetList):
    if(None != targetList):
        n = len(targetList)
        while(n > 1):
            i = 1
            while(i < n):
                if(targetList[i - 1] > targetList[i]):
                    swap(targetList, i - 1, i)
                i += 1
            n -= 1

def selectSort(targetList):
    if(None != targetList):
        for i in range(len(targetList) - 1):
            for j in range(len(targetList)):
                if(targetList[i] > targetList[j]):
                    swap(targetList, i ,j)

def insertSort(targetList):
    if(None != targetList):
        i = 1
        while(i < len(targetList)):
            itemToInsert = targetList[i]
            j = i - 1
            while(j >= 0):
                if(targetList[j] > itemToInsert):
                    targetList[j + 1] = targetList[j]
                    j -= 1
                else:
                    break
            targetList[j + 1] = itemToInsert
            i += 1

def binarySearchHelper(targetList, left, right, elementToSearch):
    if(left <= right):
        middle = (left + right) // 2
        if(elementToSearch == targetList[middle]):
            return middle
        elif(elementToSearch < targetList[middle]):
            return binarySearchHelper(targetList, left, middle, elementToSearch)
        else:
            return binarySearchHelper(targetList, middle + 1, right, elementToSearch)
    return -1

def binarySearch(targetList, elementToSearch):
    if(None != targetList):
        return binarySearchHelper(targetList, 0, len(targetList) - 1, elementToSearch)


def main():
    pass

if "__main__" == __name__:
    main()