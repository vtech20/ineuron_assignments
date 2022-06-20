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

logging.basicConfig(level=logging.DEBUG,filename="array_split.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class array_split:
    
    def __init__(self,a,num_of_split):
        self.a = a
        self.num_of_split = num_of_split

    
    def split_array(self):
        arr1 = self.a
        n = len(self.a)
        arr1[:] = arr1[self.num_of_split:n]+arr1[0:self.num_of_split]
        return arr1
        
    

try:
    a = eval(input("Enter the array : "))
    nor = int(input("Number of Split :"))
    my_ar = array_split(a,nor)
    split_of_the_array = my_ar.split_array()
    print("Rotation of the array ", split_of_the_array)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))