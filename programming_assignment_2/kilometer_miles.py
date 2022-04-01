# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 12:31:40 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_km_mi.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class kilometer_miles:
    
    def __init__(self,x):
        self.x = x
    
    def km_mi(self):
        return self.x/1.609
        
    

try:
    x = int(input("Enter the number in kilometer "))
    kmm = kilometer_miles(x)
    print("The convertion value is {} miles".format(str(kmm.km_mi())))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))