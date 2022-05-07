# -*- coding: utf-8 -*-
"""
Created on Fri May  6 21:40:37 2022

@author: vr19
"""


import logging

logging.basicConfig(level=logging.DEBUG,filename="log_fibonacci.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Python program to display the Fibonacci sequence

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

try:
    nterms = int(input("Enter number of terms - "))

    # check if the number of terms is valid
    if nterms <= 0:
        print("Plese enter a positive integer")
    else:
        print("Fibonacci series:")
        for i in range(nterms):
            print(fibonacci(i))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))