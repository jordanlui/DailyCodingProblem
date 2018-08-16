# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 14:12:30 2018

@author: Jordan

Following code solves the water fill problem and should be O(N) for time 
and O(1) for space if the max1 max2 var are removed.
They are left in here for readability of the code
"""

from waterfillSolver import waterfillSolver

def p30fill(list):
	fillcount = 0
	for i in range(1,len(list)-1):
		max1 = max(list[0:i])
		max2 = max(list[i+1:])
		if list[i] < max1 and list[i] < max2:
			fillcount += min(max1,max2) - list[i]
	return fillcount


print waterfillSolver([3,0,1,3,0,5])
print waterfillSolver([2,1,2])
print waterfillSolver([3,0,0,1,2,0,0,2,0,3])

print waterfillSolver([3,0,1,3,0,5])