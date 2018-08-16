# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 22:39:19 2018

@author: Jordan
Daily Coder 68: Bishop Diagonal
"""

# Functions
def boolBishopAttack(b1,b2):
	# Check if two bishops can attack
	# Bishops can attack if slope between them is 1 or -1
	m = (b2[1]-b1[1]) / ((b2[0]-b1[0]) * 1.0)
	if m == -1 or m == 1:
		print m
		return 1
		
	return 0

def calcNumBishopAttacks(bishops):
	# Loop through list of bishop position tuples and count number of attacks
	numAttack = 0
	M = len(bishops)
	for i in range(M):
		for j in range(i+1,M):
			if i!=j: # shouldn't happen if we loop j from i+1 to M
				if boolBishopAttack(bishops[i],bishops[j]):
					numAttack = numAttack + 1
					print 'yes',i,j
	
	
	return numAttack


# Inputs
bishops = [(0,0),
	   (1,2),
	   (2,2),
	   (4,0)]

print calcNumBishopAttacks(bishops)