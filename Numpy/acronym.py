# -*- coding: utf-8 -*-
"""
Created on Mon May 13 21:53:07 2024

@author: Nishant
"""

user_input=str(input("ask for user text:"))
text=user_input.split()
a=" "
for i in text:
    a=a+str(i[0]).upper()
    
print(a)
