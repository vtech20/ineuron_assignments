# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:29:02 2022

@author: vr19
"""
import random
import logging

logging.basicConfig(level=logging.DEBUG,filename="log_rand_numbers.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class random_num:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def rand_numbers(self):
        return random.randint(self.x,self.y)
        
    

try:
    x = int(input("Enter the lower limit to fetch random number "))
    y = int(input("Enter the upper limit to fetch random number ")) 
    rn = random_num(x,y)
    print("The Generated random number is {}".format(str(rn.rand_numbers())))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))