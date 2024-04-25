# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:01:17 2024

@author: Nishant
"""

"""

python programme to swap first and last elemnt in a list
"""


# Python3 program to swap first
# and last element of a list
 
# Swap function
def swapList(newList):
    size = len(newList)
     
    # Swapping 
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))