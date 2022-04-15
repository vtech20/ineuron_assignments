# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:00:47 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_ascii.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class ascii_value:
    
    def __init__(self,chr):
        self.chr = chr
    
    def convert(self):
        print("The ASCII value of '" + self.chr + "' is", ord(self.chr))            
            
                
try:
    a = input("Enter a character ")
    av = ascii_value(a)
    av.convert()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))