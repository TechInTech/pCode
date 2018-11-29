#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File: em.py
Description: This file emulates one emergency schedule system in hospital 
Author: Larry Yu
Initial Date: Nov 25th, 2018
"""
import sys
sys.path.append("/cygdrive/f/pCode")
from pQueue.queue import Queue
from pComparable.comparable import Comparable

#Const
rankDictionary = {1:"Critical", 2:"Serious", 3:"Fair"}


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

    def __init__(self, name, condition):
        self._name = name
        self._condition = condition
    
    def __ge__(self, other):
        return self._condition >= other._condition

    def __str__(self):
        return str(self._name) + " / " + str(self._condition)


class ERModel(object):
    def __init__(self):
        self._priorityQueue = Queue()
        self._patientNum = 0

    def isEmpty(self):
        return 0 == self._patientNum
    
    def handlePatient(self, patient):
        self._priorityQueue.enQueue(patient)

    def treatNext(self):
        return None


class ERView(object):
    """
    The view class for the ER application.
    """

    def __init__(self, model):
        self._model = model

    def _schedule(self):
        """Obtain patient's information and schedule the patient."""
        name = input("Please input the patient's name.\n")
        rank = self._getCondition()
        if 4 == rank:
            return
        else:
            patient = Patient(name, Condition(rank))
            if None != self._model:
                self._model.handlePatient(patient)
                print("Patient: %s has been handled under condtion: %s!" % (name, rankDictionary[rank]))

    def _treatNext(self):
        """Treat one patient if there is one."""
        if self._model.isEmpty():
            print("No more patients in queue!")
        else:
            patient = self._model.treatNext()
            print(patient, "is being treated.\n")
    
    def _treatAll(self):
        pass

    def _getCondition(self):
        prompt = "Please input the patient's condition:\n" + \
                 "1. Critical.\n" + \
                 "2. Serious.\n" + \
                 "3. Fair.\n" + \
                 "4. Cancel."
        try:
            userInput = int(input(prompt))
            if not userInput in range(1, 5):
                self._getCondition()
            else:
                return userInput
        except ValueError:
            self._getCondition()
        
                 

    def run(self):
        """Menu driven command loop for the app"""
        menu = "Main menu\n" + \
               "1. Schedule a patient.\n" + \
               "2. Treat the next patient.\n" + \
               "3. Treat all patients.\n" + \
               "4. Exit the program.\n"

        while True:
            command = self._getCommand(4, menu)
            if 1 == command:
                self._schedule()
            elif 2 == command:
                self._treatNext()
            elif 3 == command:
                self._treatAll()
            else:
                break    

        
    def _getCommand(self, high, menu):
        """
        Obtains and return a command number.
        """
        userInput = ""
        prompt = "Enter a number [1-" + str(high) + "]:\n"
        try:
            userInput = int(input(prompt + menu))
            if userInput not in range(1, high + 1):
                print("The input must be an intenger between 1 and %d\n" % high)
                self._getCommand(high, menu)        
        except ValueError:
            print("The input must be an intenger between 1 and %d\n" % high)
            self._getCommand(high, menu)
        
        return userInput
        

def main():
    model = ERModel()
    view = ERView(model)
    view.run()

if "__main__" == __name__:
    main()