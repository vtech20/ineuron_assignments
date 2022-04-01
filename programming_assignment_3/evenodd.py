# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:29:49 2022

@author: vr19
"""

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

logging.basicConfig(level=logging.DEBUG,filename="log_quad_equation.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class evenodd:
    
    def __init__(self,a):
        self.a = a

    
    def check_oddeven(self):
        if self.a%2 == 0:
            print('The number {} is even'.format(self.a))
        else:
            print('The number {} is Odd'.format(self.a))
        
    

try:
    a = int(input("Enter the positive number to identify even or odd "))
    eo = evenodd(a)
    eo.check_oddeven()
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))