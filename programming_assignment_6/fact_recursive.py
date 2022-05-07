# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:45:56 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_factorial.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Python program to display the Fibonacci sequence

def fact(n):
   if n>=0 and n<2:
       return 1
   else:
       return(n*fact(n-1))

try:
    n = int(input("Enter number to find factorial - "))

    # check if the number of terms is valid
    if n < 0:
        print("Plese enter a positive integer. Negative numbers cannot have factorial")
    else:
        print("Factorial of the given number {} is {}".format(n,fact(n)))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))