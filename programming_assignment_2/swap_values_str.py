# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:23:15 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_swap_numbers.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class swap_values_str:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def swap(self):
        print("The value of x before swap is {} and y is {}".format(self.x,self.y))
        self.y, self.x = self.x,self.y
        print("The value of x after swap is {} and y is {}".format(self.x,self.y))
        
    

try:
    x = input("Enter the first string ")
    y = input("Enter the second string ")
    sw = swap_values_str(x,y)
    sw.swap()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))