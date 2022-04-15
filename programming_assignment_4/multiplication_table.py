# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:26:27 2022

@author: vr19
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:12:38 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_mult_table.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class multiplication_table:
    
    def __init__(self,num):
        self.num = num
    
    def disp_table(self):
        for i in range(1,11):
            print(self.num , " X " , i , " = " , self.num*i)
                
    

try:
    b = int(input("Enter the number to display multiplication table "))
    mt = multiplication_table(b)
    mt.disp_table()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))