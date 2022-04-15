# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 19:59:58 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_armstrong.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class armstrong:
    
    def __init__(self,lower,upper):
        self.lower = lower
        self.upper = upper
    
    def disp_arm(self):
        for num in range(self.lower,self.upper + 1):
            sum1 = 0
            order = len(str(num))
            temp = num
            while temp > 0:
                digit = temp % 10
                sum1 +=digit **order
                temp //= 10
            if num == sum1:
                print(num," is an armstrong number")

try:
    a = int(input("Enter a lower limit "))
    b = int(input("Enter a upper limit" ))
    ast = armstrong(a,b)
    ast.disp_arm()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))