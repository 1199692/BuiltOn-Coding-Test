# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 07:29:43 2020

@author: Kishan
"""

#maxProduct is a function to find out the highest product of 3 numbers from given integer list num
def maxProduct(num):
    n=len(num)      
    # if size of num is less than 3, no highest product can be calculated  
    if n < 3: 
        return 'Please provide atleat 3 numbers to calculate the highest product'
  
    # Sort the list in ascending order  
    num.sort() 
  
    # Logic to return the Highest product of 3 numbers from the list  
    return max(num[0] * num[1] * num[n-1],  
               num[n-1] * num[n - 2] * num[n - 3])
