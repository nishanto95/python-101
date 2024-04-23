# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:55:59 2024

@author: Nishant
""" 

"""
Problem Statement:

Given the row count of a square array and an integer number k,

return a 2D square array where

all diagonal elements are k and
all non-diagonal elements are 0.


Input has two lines.
First line corresponds to the row count.
Second line is the integer k.

Output Format:

A 2D square array
Sample Input:

3
300
"""

import numpy as np

def k_array(row_count, k):
    '''
    INPUT : row_count, k 
    
    OUTPUT: result -> 2D array
    '''
    arr = np.eye(row_count,row_count,dtype = 'int')
    result = arr*k
    
    ## CODE STARTS HERE
    
    
    ## CODE ENDS HERE
    
    return result



