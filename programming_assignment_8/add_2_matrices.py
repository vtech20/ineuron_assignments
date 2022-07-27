# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="add_2_matrices.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

try:
    X = [[12,7,3],
         [4 ,5,6],
         [7 ,8,9]]
    
    Y = [[5,8,1],
         [6,7,3],
         [4,5,9]]

    result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

    for r in result:
        print(r)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))