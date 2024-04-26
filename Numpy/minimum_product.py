# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:59:12 2024

@author: Nishant
"""

"""
minimum product pair in a list
"""
def min_product(numbers):
    if len(numbers) < 2:
        return None  # Minimum product not possible with less than 2 elements
    
    min_prod = float('inf')  # Initialize minimum product to positive infinity
    
    # Iterate through all pairs of numbers in the list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]  # Calculate the product of the pair
            min_prod = min(min_prod, product)