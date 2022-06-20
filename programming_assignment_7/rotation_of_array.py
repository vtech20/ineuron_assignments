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

logging.basicConfig(level=logging.DEBUG,filename="array_rotation.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class array_rotation:
    
    def __init__(self,a,num_of_rotations):
        self.a = a
        self.num_of_rotations = num_of_rotations

    
    def rotate_array(self):
        arr1 = self.a
        n = len(self.a)
        arr1[:] = arr1[self.num_of_rotations:n]+arr1[0:self.num_of_rotations]
        return arr1
        
    

try:
    print(" Executing Rotation of Array")
    a = eval(input("Enter the array : "))
    nor = int(input("Number of Rotations :"))
    my_ar = array_rotation(a,nor)
    rotation_of_the_array = my_ar.rotate_array()
    print("Rotation of the array ", rotation_of_the_array)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))