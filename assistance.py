# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:05:05 2019

Course:     COMP 2210 - F 19
Professor:  A. Mohd
@author:    Ivan Belov
Student ID: T00637195
Project:    Lab three
Due Date: September 25, 10:00 PM
Questions two
assistance.py is in charge of calculating non-government assistance.

5772697474656e206279204976616e2042656c6f762e2
0416c6c207269676874732072657365727665642e2053
686172656420666f72206c6561726e696e67207075727
06f736573206f6e6c792e204e6f7420696e2063686172
6765206f6620706c616769617269736d20617474656d7
07420627920612074686972642d70617274792e

"""

TRIPNUMBER = -1

# function one - infoRequest
def infoRequest():
    annualHouseholdIncome = float(input( " Enter your house hold income: ( -1 to quit ) " ))
    children = int(input( " How many children do you have? " ))
    return annualHouseholdIncome
    return children

# function two - calculateAssistance
def calculateAssistance(passedAnnualIncome, passedChildrenNum):
    if ((passedAnnualIncome >= 30000 | passedAnnualIncome <= 40000 ) & ( passedChildrenNum >= 3 )):
        incomeAssistance = 1000
    if ((passedAnnualIncome >= 20000 | passedAnnualIncome < 30000 ) & ( passedChildrenNum >= 2 )):
        incomeAssistance = 1500
    if ( passedAnnualIncome < 20000 ):
        incomeAssistance = passedChildrenNum * 2000
    return incomeAssistance

#function three - printAssistance
def printAssistance(passedIncomeAssistance):
    print( " Your assistance is: $ " )
    print(passedIncomeAssistance)
    
# main function
def main():
    printAssistance(calculateAssistance(infoRequest(), infoRequest()))

# start execution here
main()
