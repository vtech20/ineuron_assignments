# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="binarystring.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class binarystring:

    def __init__(self,text):
        self.text = text

    def binary_string(self):
        try:
        # this will raise value error if
        # string is not of base 2
            int(self.text, 2)
            print("Yes it is a Binary String")
        except ValueError:
            print("No it is not a Binary String")
        

try:
    text = input("Enter the string : ")
    bs = binarystring(text)
    bs.binary_string()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))