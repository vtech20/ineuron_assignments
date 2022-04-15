# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:12:38 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_factorial.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class factorial:
    
    def __init__(self,num):
        self.num = num
    
    def fact(self):
        facto = 1
        if self.num == 1 or self.num==0:
            return 1
        elif self.num < 0:
            print("Cannot find factorial of negative numbers")
        else:
            for i in range(1,self.num + 1):
                facto = facto * i
            return facto
                
    

try:
    b = int(input("Enter the number to find factorial "))
    fc = factorial(b)
    print("The factorial of number {} is : {}".format(b,str(fc.fact())))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))