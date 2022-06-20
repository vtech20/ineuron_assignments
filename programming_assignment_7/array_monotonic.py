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

logging.basicConfig(level=logging.DEBUG,filename="monotonic.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class monotonic:
    
    def __init__(self,a):
        self.a = a
        

    
    def is_monotonic(self):
        return (all(self.a[i] <= self.a[i + 1] for i in range(len(self.a) - 1)) or
            all(self.a[i] >= self.a[i + 1] for i in range(len(self.a) - 1)))
        
    

try:
    a = eval(input("Enter the array : "))
    my_mo = monotonic(a)
    monotonic_array = my_mo.is_monotonic()
    print("monotonic of the array ", monotonic_array)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))