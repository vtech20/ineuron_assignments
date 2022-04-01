# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:32:33 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_area_triangle.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class area_triangle:
    
    def __init__(self,b,h):
        self.b = b
        self.h = h
    
    def area_triangle(self):
        a = 0.5 * self.b * self.h
        return a
    

try:
    b = int(input("Enter the base value "))
    h = int(input("Enter the height value ")) 
    at = area_triangle(b,h)
    print("The area of triangle is : {}".format(str(at.area_triangle())))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))