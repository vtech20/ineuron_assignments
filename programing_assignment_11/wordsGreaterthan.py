# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="wordsgreaterthan.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class wordsgreaterthan:

    def __init__(self,text,number):
        self.text = text
        self.number = number

    def wordsGreaterthan(self):
        wordList= self.text.split(" ")
        wordsgtthan =[]
        for i in wordList:
            if len(i)>self.number:
                wordsgtthan.append(i)
        print(f'Words > length {self.number} in "{self.text}" \n {wordsgtthan}')

try:
    text = input("Enter the string : ")
    number = int(input("Enter the number to find the words greater than this? "))
    wgt = wordsgreaterthan(text,number)
    wgt.wordsGreaterthan()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))