# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:19:24 2024

@author: Nishant
"""

"""
Given a NumPy array, return the index of the first element that is greater than
 the target passed as an argument.

Return -1, if there isn't any element greater than the target.

Input Format:

First line will have a list which is later typecasted to NumPy array
Second line will have an integer representing target
Output Format:

A NumPy array consisting of one index
Sample Input:

arr = [-1,2,3,-4,5]
target = 3

"""
import numpy as np
def first_greater(arr, target):
    '''arr -> A numpy array
       target -> An integer
       Output -> A numpy array consisting of an index should be returned'''
    
    # YOUR CODE GOES HERE
    #mask_target = np.where(arr==target)[0][0]
    #print(mask_target)




    
    #print(np.where(arr>target)[0])
    #print(np.where(arr>target))
    try:
        return [np.where(arr>target)[0][0]]

    except:
        pass
    return -1





                        