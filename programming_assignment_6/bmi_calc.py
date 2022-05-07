# -*- coding: utf-8 -*-
"""
Created on Fri May  6 22:34:20 2022

@author: vr19
"""

import logging

logging.basicConfig(level=logging.DEBUG,filename="log_bmi.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class bmi:
    
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    
    def disp_bmi(self):
        if self.weight <= 0 or self.height <= 0:
            print('Please enter proper weight or height')
            return None
        else:
            BMI = self.weight / (self.height/100)**2
            print(f"You BMI is {BMI}")
            dct = {18.4:'underweight',24.9:'healthy',29.9:'overweight',34.9:'Too much overweight',39.9:'obese'}
            for key,val in dct.items():
                if BMI <= key:
                    return val
            else:
                return "Severe Obese"
            
                
    

try:
    while True:
        height = int(input("Enter your height in cms "))
        weight = int(input("Enter your weight in kgs "))
        bm = bmi(height,weight)
        bmi_stat = bm.disp_bmi()
        if bmi_stat != None:
            print(f"you are {bmi_stat}.")
            break
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))