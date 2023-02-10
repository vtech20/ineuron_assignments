# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="splitjoin.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class splitjoin:

    def __init__(self,text,number):
        self.text = text
        self.number = number

    def split_join(self):
        print(f"old_string : {self.text}")
        str1 = self.text[:self.number]
        str2 = self.text[self.number:]
        print(f"split strings: 1. {str1} \n 2. {str2}")



try:
    text = input("Enter the string : ")
    number = int(input("Enter the nth character to split "))
    sj = splitjoin(text,number)
    sj.split_join()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))