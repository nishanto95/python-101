# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 21:59:38 2024

@author: Nishant
"""

"""
Given a NumPy array of integer elements, write a program that calculates the sigmoid value of each of those elements and returns these sigmoid values rounded up to 2 decimal places in a NumPy array.

The value of sigmoid function for an element x is:

Sigmoid(x) =  
(1+e 
−x
 )
1
​
 

Input Format:

A list of integers is taken as input which is then typecasted to NumPy array and passed as an argument.
Output Format:

A NumPy array with float values rounded off to two decimal places.
Sample Input:

[-2, -1, 0, 1, 2]
"""

import numpy as np
def sigmoid(arr):
    '''arr -> A numpy array
       Output -> A numpy array of same dimensions as arr is expected to be returned'''
    import math
    ## STEP 1: Calculate exponent of -ve x
    
    z = np.exp(-arr)
    
    ## STEP 2: Calculate denominator (1 + z) where z = e^-x
    
    denom = 1+z
    
    ## Calculate sigmoid using numerator and denominator
    
    result = 1/denom
    
    ## Round off the values to two decimal places
    
    result = np.round(result,2)
    
    return result