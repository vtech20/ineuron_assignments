# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging
import re

logging.basicConfig(level=logging.DEBUG,filename="special_chars.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class specialchar:

    def __init__(self,string1):
        self.string1 = string1

    def check_special(self):
        special_char = re.compile('[@_!#"$%^&*()<>?/\|}{~:]')
        chars = special_char.findall(self.string1)
        print(f'Special characters found {chars}') 
        

try:
    string1 = input("Enter the string : ")
    sc = specialchar(string1)
    sc.check_special()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))