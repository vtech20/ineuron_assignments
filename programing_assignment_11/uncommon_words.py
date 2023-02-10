# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="uncommon_words.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class uncommon:

    def __init__(self,string1,string2):
        self.string1 = string1
        self.string2 = string2

    def uncommon_words(self):
        str1=self.string1.split()
        str2=self.string2.split()
        k=set(str1).symmetric_difference(set(str2))
        return k
        

try:
    string1 = input("Enter the string 1 : ")
    string2 = input("Enter the string 2 : ")
    u = uncommon(string1,string2)
    print(u.uncommon_words())
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))