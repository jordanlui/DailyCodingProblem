# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:40:18 2018

@author: Jordan
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Note the following solution doesn't use division
"""

def prodOthers(list):
    # Product of all others in list
    # Initialize product
    prod = []
    # Iterate through length of list
    for i,num in enumerate(list):
        # For each item, grab the other elements and calculate product
        prod.append(listProduct(list[:i] + list[i+1:]))
    return prod

def prodOthersDivision(list):
    # Use product and division for easy solve
    totalProduct = listProduct(list)
    prod = []
    for i,num in enumerate(list):
        prod.append(totalProduct / num)
    return prod

def listProduct(list):
    # Product of elements in list
    p = 1
    for i in list:
        p *= i
    return p

# Main Loop
list = [1,2,3,4,5]
print prodOthers(list)
print prodOthersDivision(list)