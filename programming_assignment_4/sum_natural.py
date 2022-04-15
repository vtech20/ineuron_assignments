# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:09:18 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_sum_natural.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class sum_natural:
    
    def __init__(self,num):
        self.num = num
    
    def disp_sum(self):
        if self.num < 0:
            print("Entered number is a negative number")
        else:
            sum1 = 0
            while (self.num > 0):
                sum1 += self.num
                self.num -= 1
            print("The sum of the natural number is ", sum1)
                

try:
    a = int(input("Enter a number "))
    snat = sum_natural(a)
    snat.disp_sum()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))