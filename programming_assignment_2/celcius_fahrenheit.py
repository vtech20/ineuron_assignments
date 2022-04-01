# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 14:54:40 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_c_to_f.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class celcius_fahrenheit:
    
    def __init__(self,x):
        self.x = x
    
    def cs_ft(self):
        return (self.x*1.8) + 32
        
    

try:
    x = int(input("Enter the temperature in Celcius "))
    cf = celcius_fahrenheit(x)
    print("The converted fahrenheit value is {}".format(str(cf.cs_ft())))
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))