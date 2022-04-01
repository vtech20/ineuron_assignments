# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:26:10 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_numcheck.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class numcheck:
    
    def __init__(self,x):
        self.x = x
    
    def check(self):
        if self.x > 0:
            print("The given number is positive")
        elif self.x == 0:
            print("The given number is zero")
        else:
            print("The given number is negative")
        
    

try:
    x = int(input("Enter a number "))
    nc = numcheck(x)
    nc.check()
    
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))