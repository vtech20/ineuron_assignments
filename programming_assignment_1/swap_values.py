# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:51:19 2022

@author: vr19
"""


import logging

logging.basicConfig(level=logging.DEBUG,filename="log_swap_numbers.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class swap_values:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def swap(self):
        print("The value of x before swap is {} and y is {}".format(self.x,self.y))
        self.y, self.x = self.x,self.y
        print("The value of x after swap is {} and y is {}".format(self.x,self.y))
        
    

try:
    x = int(input("Enter the first number "))
    y = int(input("Enter the second number ")) 
    sw = swap_values(x,y)
    sw.swap()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))