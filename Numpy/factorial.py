# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:12:39 2024

@author: Nishant
"""
Factorial of a non-negative integer,
 is multiplication of all integers smaller than or equal to n.
"""
# Python 3 program to find  
# factorial of given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num)