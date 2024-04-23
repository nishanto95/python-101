# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:01:50 2024

@author: Nishant
"""

"""
Problem Statement:

Given a 1D array, return the first and last elements from the array.
Input Format:

A 1D numpy array
Output Format:

A tuple (first_element, last_element)
Sample Input:

[0, 1, 2, 3, 4, 5]
"""
import numpy as np

def get_elements(arr):
    '''
    INPUT: arr -> 1D numpy array
    
    OUTPUT elements -> tuple of first and last element.
    '''
    
    first_element = arr[0]
    
    last_element = arr[-1]
    
    return (first_element, last_element)