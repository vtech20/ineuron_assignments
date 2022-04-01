# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""

import logging
import datetime
import calendar

logging.basicConfig(level=logging.DEBUG,filename="log_calendar.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class my_calendar:
    
    def __init__(self,month,year):
        self.month = month
        self.year = year
    
    def cal(self):
        print(calendar.month(self.year, self.month))
        
    

try:
    today = str(datetime.date.today())
    curr_year = int(today[:4])
    curr_month = int(today[5:7])
    cal_now = my_calendar(curr_month,curr_year)
    cal_now.cal()
    x = input("Would you like to display some other month/year? Press Y/N ")
    if x.lower() == 'y':
        yy = int(input("Enter the year you would like to show "))
        mm = int(input("Enter the month you would like to show "))
        cal_special = my_calendar(mm,yy)
        cal_special.cal()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))