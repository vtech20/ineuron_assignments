# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 21:28:32 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="log_arithmetic_operation.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class arithmetic_operation:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        self.c = self.a + self.b
        return self.c
    
    def sub(self):
        self.c = self.a - self.b
        return self.c
    
    def mul(self):
        self.c =self.a * self.b
        return self.c
    
    def div(self):
        try:
            self.c = self.a/self.b
        except ZeroDivisionError:
            logging.exception("Cannot be divide by 0")
        except Exception as e:
            logging.exception("Exception occured while performing operations"+str(e))



try:
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    option = int(input("Enter the operation you need to perform : press 1 - Add, 2 - Sub, 3 - Mul, 4 - Div "))
    e = arithmetic_operation(a,b)
    if option==1:
        c = e.add()
        print("The sum of {} and {} is {}".format(a,b,c))
    elif option==2:
        c = e.sub()
        print("The difference of {} and {} is {}".format(a,b,c))        
    elif option==3:
        c = e.mul()
        print("The multiple of {} and {} is {}".format(a,b,c))    
    elif option==4:
        c = e.div()
        print("The division of {} and {} is {}".format(a,b,c))
except Exception as e:        
    logging.exception("Exception occured while performing operations"+str(e))
            