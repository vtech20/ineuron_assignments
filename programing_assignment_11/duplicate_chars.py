# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="duplicate_chars.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class duplicate:

    def __init__(self,string1):
        self.string1 = string1

    def duplicate_chars(self):
        duplicates = []
        for char in self.string1:
            if self.string1.count(char)>1:
                if char not in duplicates:
                    duplicates.append(char)
        print(duplicates)
        

try:
    string1 = input("Enter the string 1 : ")
    d = duplicate(string1)
    d.duplicate_chars()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))