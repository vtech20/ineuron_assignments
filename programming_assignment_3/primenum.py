# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:39:13 2022

@author: vr19
"""


import logging

logging.basicConfig(level=logging.DEBUG,filename="log_primenum.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class primenum:
    
    def __init__(self,a):
        self.a = a
    
    def check_prime(self):
        f = False
        if self.a > 1:
            for i in range(2,self.a):
                if (self.a % i) == 0:
                    f = True
                    break
        if f:
            print("The given number {} is not a prime number".format(self.a))
        else:
            print("The given number {} is a prime number".format(self.a))
                    
            
        
    

try:
    x = int(input("Enter the number "))
    pn = primenum(x)
    pn.check_prime()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))