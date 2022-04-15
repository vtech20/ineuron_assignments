# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:41:19 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_hcf.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class hcf:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def calc_hcf(self):
        hcf = 1
        for i in range(2,self.num1+1):
            if (self.num1 % i == 0 and self.num2 % i == 0):
                hcf = i
        print("The HCF of 2 numbers {} and {} is {}".format(self.num1,self.num2,hcf))
            
                
try:
    a = int(input("Enter a first number "))
    b = int(input("Enter a second number "))
    h = hcf(a,b)
    h.calc_hcf()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))