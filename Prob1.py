# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 21:54:00 2018

@author: Jordan
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Hash table (Python Dictionary) allows us to do this in one pass
"""


list = [10,15,3,7]
k = 17
diffs = {}

def complementInList(list):
    # Check if complement value exists in list
    for i,item in enumerate(list):
        diffs[item] = k-item
        print diffs
        if k-item in diffs:
            return True
        
    return False

print complementInList(list)
