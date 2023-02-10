# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="removeithchar.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class removeithchar:

    def __init__(self,text,number):
        self.text = text
        self.number = number

    def remove_char(self):
        new_str =""
        for i in range(len(self.text)):
            if i != self.number:
                new_str +=  self.text[i]
        print(new_str)


try:
    text = input("Enter the string : ")
    number = int(input("Enter the ith character to remove "))
    ric = removeithchar(text,number)
    ric.remove_char()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))