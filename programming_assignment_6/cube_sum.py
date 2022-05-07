# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:02:22 2022

@author: vr19
"""

import logging
import math

logging.basicConfig(level=logging.DEBUG,filename="log_cube_sum.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class cube_sum:
    
    def __init__(self,num):
        self.num = num
    
    def disp_cube_sum(self):
        c_sum = 0
        for i in range(1,self.num+1):
            c_sum+=i*i*i
        return c_sum
            
                
    

try:
    num = int(input("Enter number to find cube sum of series "))
    cs = cube_sum(num)
    cube_sum = cs.disp_cube_sum()
    print("Cube Sum of {} is {}".format(num,cube_sum) )
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))