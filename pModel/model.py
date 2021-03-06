#!/usr/bin/python3
#-*-coding:utf-8-*-

"""
File: model.py
Description: This file implements the class model
Author: Larry Yu
Initial Date: 18th Nov, 2018
"""

import random
import sys
sys.path.append("/cygdrive/d/repo/pCode/")
from pQueue.queue import Queue

#Const
TOTOAL_RUNNING_TIME_PROMPT = "Please input the total seconds (1-100) this model to run or type 'exit' to exit:\n"
AVERAGE_TIME_PER_CUSTOMER = "Please input the average seconds (1-3) each customer takes or type 'exit' to exit:\n"
CUSTOMER_APPEAR_PROBABILITY = "Please input the probability (0.1-0.9) that customer arrives or type 'exit' to exit:\n"
WELCOME_PROMPT = "Welcome to the market simulator!\n\n"


#Publc function
def inputAndCheckParameter(prompt, expectType, *expectRange):
    paraValue = input(prompt)
    if type(paraValue) == str and paraValue == "exit":
        exit(0)
    else:
        try:
            retValue = expectType(paraValue)
            if None != expectRange:
                min = expectRange[0]
                max = expectRange[1]
                if(not retValue >= min and retValue <= max):
                    print("Parameter out of range, the min=%s, max=%s\n" % (str(min), str(max)))
                    inputAndCheckParameter(prompt, expectType, *expectRange)
                    
            return retValue
        except ValueError as e:
            print(e)
            inputAndCheckParameter(prompt, expectType, *expectRange)

class Customer(object):

    @classmethod
    def generateCustomer(cls, probabilityOfNewArrival,
                         arrivalTime,
                         averageTimePerCustomer):
        if(random.random() <= probabilityOfNewArrival):
            return Customer(arrivalTime, averageTimePerCustomer)
        else:
            return None

    def __init__(self, arrivalTime, serviceNeeded):
        self._arrivalTime = arrivalTime
        self._amountServiceNeeded = serviceNeeded

    def Served(self):
        if(self._amountServiceNeeded > 0):
            self._amountServiceNeeded -= 1
    
    def arriveTime(self):
        return self._arrivalTime
    
    def amountOfServiceNeed(self):
        return self._amountServiceNeeded

class Cashier(object):
    """
    To represent the class "Cashier"
    """
    def __init__(self):
        self._totalCustomerWaitTime = 0
        self._numnerOfCustomerServed = 0
        self._currentCustomer = None
        self._customerQueue = Queue()

    def addCustomer(self, c):
        if(None != self._customerQueue):
            self._customerQueue.enQueue(c)
    
    def serveCustomer(self, currentTime):
        #Not able to serve multi-customers at the same time
        if None == self._currentCustomer:
            #No customer now
            if self._customerQueue.isEmpty():
                return
            #To serve customers if the queue is not empty
            else:
                self._currentCustomer = self._customerQueue.deQueue()
                self._totalCustomerWaitTime += currentTime - self._currentCustomer.arriveTime()

        #Send a signal to customer.
        self._currentCustomer.Served()

        #Finish serving customer, and release the resource
        if(0 == self._currentCustomer.amountOfServiceNeed()):
            self._currentCustomer = None
            self._numnerOfCustomerServed += 1


    def __str__(self):
        printStr = "TOTALS FOR THE CASHIER\n" + \
        "Number of customer servered: \n" + \
        str(self._numnerOfCustomerServed) + "\n"
        if(0 != self._numnerOfCustomerServed):
            aveWaitTime = self._totalCustomerWaitTime / self._numnerOfCustomerServed
            printStr += "Number of cutomer in queue: \n" + str(len(self._customerQueue)) + "\n" \
            + "Average time customer spent " + \
            "waitting to be servered: \n" + \
            "%-5.2f" % aveWaitTime

        return  printStr


class MarketModel(object):
    """
    This class will do:
        1. Maintain an virtual clock which drives the whole market system to run.
        2. Generate one cashier.
        3. Save the input parameters from terminal
    """
    #Class const variables
    def __init__(self, totalTime2Run, averageServeTimePerCus, probobilityOfNewArrival):
        self._totalTime2Run = totalTime2Run
        self._averageServeTimePerCus = averageServeTimePerCus
        self._probobilityOfNewArrival = probobilityOfNewArrival
        self._cashier = Cashier()

    def runSimulation(self):
        """
        This function does generate signal which drives the simulation
        """
        #The current stands for a tick in clock, and it is sent to cashier as the signal to serve customers
        for currentTime in range(self._totalTime2Run):
            #Try to generage a customer
            customer = Customer.generateCustomer(self._probobilityOfNewArrival, currentTime, self._averageServeTimePerCus)
            #Add customer into chashier's queue
            if None != customer:
                self._cashier.addCustomer(customer)
            
            #Receive signal from clock and process 
            self._cashier.serveCustomer(currentTime)
    
    def __str__(self):
        return str(self._cashier)

def main():
    print(WELCOME_PROMPT)

    totalRunningTime = inputAndCheckParameter(TOTOAL_RUNNING_TIME_PROMPT, int, 1, 100)
    avarageServeTimePerCustomer = inputAndCheckParameter(AVERAGE_TIME_PER_CUSTOMER, int, 1, 3)
    probabilityOfCustomerArrival = inputAndCheckParameter(CUSTOMER_APPEAR_PROBABILITY, float, 0.1, 0.9)

    #To initial market object
    market = MarketModel(totalRunningTime, avarageServeTimePerCustomer, probabilityOfCustomerArrival)
    market.runSimulation()
    print(market)

if "__main__" == __name__:
    main()