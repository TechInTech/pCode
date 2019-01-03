"""
File: hashtable.py
Description: This file implements the class hashtable and some test functions as auxliary
Author: Larry Yu
Initiated Data: Jan 2nd, 2019
"""
from pArray.arrays import Array

class HashTable(object):
    """
    To represent HashTable
    """

    #Class Variables
    EMPTY = None
    DELETED = True

    def __init__(self, capacity = 29, hashFunction = hash, linear = True):
        self._table = Array(capacity, HashTable.EMPTY)
        self._size = 0
        self._hashFunction = hashFunction
        self._homeIndex = -1
        self._actualIndex = -1
        self._linear = linear
        self._probeCount = 0

    def __len__(self):
        size = 0
        for item in self._table:
            if not item in (HashTable.EMPTY, HashTable.DELETED):
                size += 1
        return size        

    def insert(self, item):
        """
        To insert item into hash table 
        Precondition: There is at least one empty cell or
        one previously occupied cell.
        This is not a duplicate cell.
        """
        #The length of self._table coule never be zero, cuz it has an inital array.
        self._homeIndex = abs(self._hashFunction(item)) % len(self._table)
        distance = 1
        index = self._homeIndex
        increment = 0

        while not self._table[index] in (HashTable.EMPTY, HashTable.DELETED):
            if self._linear:
                increment = index + 1
            else:
                increment = self._homeIndex + distance**2
                distance += 1
            index = increment % len(self._table)
            self._probeCount += 1
        
        #Found an empty or deleted cell
        self._table[index] = item
        self._size += 1
        self._actualIndex = index
    
    def loadFactor(self):
        """
        Returns the load factor of this hash table
        """
        return float(len(self) / len(self._table))

    def homeIndex(self):
        """
        Returns the homeIndex of the item which is just inserted
        """
        return self._homeIndex

    def actualInex(self):
        """
        Gets the actual index of the item which is just inserted.
        """
        return self._actualIndex

    def probeCount(self):
        """
        Returns the number of probe for the item which is just inserted.
        """
        return self._probeCount



class Profiler(object):
    """
    Represent a profiler for hash table.
    """

    def __init__(self):
        self._table = None
        self._collisions = 0
        self._probeCount = 0

    def test(self, table, data):
        """
        Insert the data into table and gathers statistics
        """
        self._table = table
        self._collisions = 0
        self._probeCount = 0
        self._result = "Load Factor Item Inserted " + \
                        "Home index Actual Index Probes\n"
        for item in data:
            loadFactor = table.loadFactor()
            table.insert(item)
            homeIndex = table.homeIndex()
            actualIndex = table.actualInex()
            probes = table.probeCount()
            self._probeCount += probes
            if probes > 0:
                self._collisions += 1
            line = "%8.3f%14d%12d%12d%14d" % (loadFactor, item, homeIndex, actualIndex, probes)
            self._result += line + "\n"
        
        self._result += "Total Collisions: " + \
                        str(self._collisions) + \
                        "\nTotal Probes: " + \
                        str(self._probeCount) + \
                        "\nAverage probes per collision: " + \
                        str(self._probeCount / self._collisions)

    def __str__(self):
        if None == self._table:
            return "No test has been run yet."
        else:
            return self._result

#For test purpose
def main():
    pass

if "__main__" == __name__:
    main()