# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 20:45:04 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_decimal_conversion.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class decimal_conversion:
    
    def __init__(self,num,option):
        self.num = num
        self.option = option
    
    def convert(self):
        if self.option == 'B':
            print("The converted value in Binary is {}".format(bin(self.num)))
        elif self.option == 'O':
            print("The converted value in Octal is {}".format(oct(self.num)))
        elif self.option == 'H':
            print("The converted value in Hexadecimal is {}".format(hex(self.num)))
        else:
            print("Invalid option")            
            
                
try:
    a = int(input("Enter a decimal number "))
    b = input("Enter an option to convert? type- B - Binary, O - Octal, H- Hexadecimal ")
    dc = decimal_conversion(a,b)
    dc.convert()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))