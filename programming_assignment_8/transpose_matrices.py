# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 15:00:38 2022

@author: vr19
"""
import logging

logging.basicConfig(level=logging.DEBUG,filename="transpose_matrices.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

try:
    X = [[12,7],
         [4 ,5],
         [3 ,8]]

    result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

    for r in result:
        print(r)
except Exception as e:
    logging.exception("Exception occured while performing operations"+str(e))