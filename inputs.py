# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 14:17:42 2015

@author: jack.gang
"""

def intInput(string):
    while True:        
        fromUser = raw_input(string)
        try:
            result = int(fromUser)
            return result            
        except ValueError:
            print "Please enter an integer"
            
def positiveIntInput(string):
    while True:        
        fromUser = raw_input(string)
        try:
            result = int(fromUser)
            if result >= 0:
                return result
            else:
                print "Please enter a positive integer"
        except ValueError:
            print "Please enter a positive integer"
            
def floatInput(string):
    while True:        
        fromUser = raw_input(string)
        try:
            result = float(fromUser)
            return result            
        except ValueError:
            print "Please enter a number"
            
def positiveFloatInput(string):
    while True:        
        fromUser = raw_input(string)
        try:
            result = float(fromUser)
            if result >= 0:
                return result
            else:
                print "Please enter a positive number"
        except ValueError:
            print "Please enter a positive number"