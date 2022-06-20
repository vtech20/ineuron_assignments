# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:17:08 2022

@author: vr19
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""

import logging
import cmath

logging.basicConfig(level=logging.DEBUG,filename="sum_of_array.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class soa:
    
    def __init__(self,a):
        self.a = a

    
    def sum_of_array(self):
        ans = sum(self.a)
        return ans
        
    

try:
    print(" Executing Sum of Array")
    a = eval(input("Enter the array : "))
    my_soa = soa(a)
    sum_of_the_array = my_soa.sum_of_array()
    print("Sum of the array ", sum_of_the_array)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))