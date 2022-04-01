# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:17:08 2022

@author: vr19
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""

import logging
import cmath

logging.basicConfig(level=logging.DEBUG,filename="log_quad_equation.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class my_quad_equation:
    
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def compute_quad(self):
        d = (self.b**2) - (4*self.a*self.c)
        sol1 = (-self.b-cmath.sqrt(d))/(2*self.a)
        sol2 = (-self.b+cmath.sqrt(d))/(2*self.a)
        print('The solution are {0} and {1}'.format(sol1,sol2))
        
    

try:
    print("Solving the quadratic equation ax**2 + bx + c = 0")
    a = int(input("Enter the first non zero value "))
    b = int(input("Enter the second non zero value "))
    c = int(input("Enter the third non zero value "))
    mqe = my_quad_equation(a,b,c)
    mqe.compute_quad()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))