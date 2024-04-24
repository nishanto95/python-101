# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 01:14:35 2024

@author: Nishant
"""

"""
Create a sequence of a given length from a given start point, where the difference between 2 consecutive elements of the expected sequence is also given as step.

Input Format:

One line of input will have 3 space-separated integers consisting of start, length of sequence and step between two continuous elements of the sequence.
Output Format:

A numpy array of integers
Sample Input:

5 10 3
"""
import numpy as np
def seq(start, length, step):
    ''' start, length and step are in form of integers all representing the attributes as their names suggest
        output -> A numpy array is expected to be returned'''

    # YOUR CODE GOES HERE
    
    sequence = np.arange(start,start+length*step,step)
    
    return sequence