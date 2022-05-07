# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:49:27 2022

@author: vr19
"""

import logging
import math

logging.basicConfig(level=logging.DEBUG,filename="log_natlog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class natlog:
    
    def __init__(self,num):
        self.num = num
    
    def disp_natlog(self):
        ans = math.log(self.num)
        return ans
            
                
    

try:
    num = int(input("Enter number to find natural log "))
    nl = natlog(num)
    nat_res = nl.disp_natlog()
    print("Natural log of {} is {}".format(num,nat_res) )
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))