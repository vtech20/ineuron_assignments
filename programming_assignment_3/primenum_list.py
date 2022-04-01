# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:46:24 2022

@author: vr19
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:39:13 2022

@author: vr19
"""


import logging

logging.basicConfig(level=logging.DEBUG,filename="log_primenum_list.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

class primenum_list:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def list_prime(self):
        set_prime = set()
        
        for num in range(self.x,self.y + 1):
            j = 0
            if num > 1:
                for i in range(2,num):
                    if (num % i) == 0:
                        f = True
                        j+=1
                        break
                if j > 0:
                    pass
                else:
                    set_prime.add(num)

        if not set_prime:
            print("There is no prime number between the range ")
        else:
            print("The prime numbers between the lower limit {} and upper limit {} are ".format(self.x,self.y), set_prime)
                    
            
        
    

try:
    x = int(input("Enter the lower limit number "))
    y = int(input("Enter the upper limit number "))
    pn = primenum_list(x,y)
    pn.list_prime()
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))