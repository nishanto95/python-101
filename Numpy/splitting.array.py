# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:46:57 2024

@author: Nishant
"""

"""
Given an 1D array and an integer k that specifies the number of equal parts to split the array into,

Perform the following operations:

Split the array into k number of equal parts.
Return the list of split arrays.
Assumption: The array can be split into k equal parts

Note: Recall how to split an array into equal parts
"""
def split (arr,K):
    
    split_arr=np.split(arr,k)
    return split_arr