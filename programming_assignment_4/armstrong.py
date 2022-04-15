# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:41:29 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_armstrong.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class armstrong:
    
    def __init__(self,num):
        self.num = num
    
    def disp_arm(self):
        sum1 = 0
        temp = self.num
        while temp > 0:
            digit = temp % 10
            sum1 +=digit **3
            temp //= 10
        if self.num == sum1:
            print(self.num," is an armstrong number")
        else:
            print(self.num, "is not an armstrong number")
            
                
    

try:
    b = int(input("Enter a number "))
    ast = armstrong(b)
    ast.disp_arm()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))