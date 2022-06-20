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

logging.basicConfig(level=logging.DEBUG,filename="largest_array.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class largest_array:
    
    def __init__(self,a):
        self.a = a

    
    def largest_of_array(self):
        ans = max(self.a)
        return ans
        
    

try:
    print(" Executing Largest element of Array")
    a = eval(input("Enter the array : "))
    my_la = largest_array(a)
    largest_of_the_array = my_la.largest_of_array()
    print("Largest of the array ", largest_of_the_array)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))