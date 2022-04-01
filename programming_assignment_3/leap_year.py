# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:34:08 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_leapyear.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class leap_year:
    
    def __init__(self,year):
        self.year = year
    
    def check_leap(self):
        if self.year%4 == 0:
            print("The given year is leap year")
        else:
            print("The given year is not a leap year")
        
    

try:
    x = int(input("Enter the year "))
    ly = leap_year(x)
    ly.check_leap()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))