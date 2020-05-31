#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author - Samar Srivastava (https://samacker77.github.io)
Problem Link - https://www.hackerrank.com/challenges/s10-weighted-mean/problem

Problem Statement - Given an array, X, of N integers and an array,W , representing the respective weights of X's elements,
calculate and print the weighted mean of X's elements.
 Your answer should be rounded to a scale of 1 decimal place (i.e.,12.3  format).
'''


#---------------Solution------------------#

class Solution():
    def __init__(self,X:list,W:list,N:int):
        self.X = X
        self.W = W
        self.N = N
    def inputs(self):
        return self.X,self.W,self.N
    def weighted_mean(self):
        weighted_sum = 0
        for ix in range(len(self.X)):
            weighted_sum = weighted_sum + (X[ix]*W[ix])
        return round(weighted_sum/sum(self.W),1)



N = int(input())
X = list(map(int,input().split()))
W = list(map(int,input().split()))
submit = Solution(X,W,N)
print(submit.weighted_mean())

        
            





