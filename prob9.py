# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 16:08:57 2018

@author: Jordan

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def largestNonAdjacent(list):
    # Simplify this: Largest of 2 sum piles
    sum1=0
    sum2=0
    for num in list:
        newsum = max(sum1,sum2)
        print(num,newsum,sum1,sum2)
        sum1 = sum2 + num
        sum2 = newsum
        
    print(num,newsum,sum1,sum2)
    return max(sum1,sum2)

def find_max_sum(arr):
    incl = 0
    excl = 0
    
    for i in arr:
         
        # Current max excluding i (No ternary in 
        # Python)
        new_excl = excl if excl>incl else incl
        
        # Current max including i
        incl = excl + i
        excl = new_excl
     
    # return max of incl and excl
    return(max(incl,excl))
#    return (excl if excl>incl else incl)

# Main loop
list1 = [2,4,6,2,5]
list2 = [5,1,1,5]

print largestNonAdjacent(list1)
print largestNonAdjacent(list2)

print find_max_sum([5,1,1,5])