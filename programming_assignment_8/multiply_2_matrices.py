# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="multiply_2_matrices.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

try:
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    # 3x4 matrix
    Y = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]

    # result is 3x4
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

    for r in result:
        print(r)
        
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))