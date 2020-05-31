#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author - Samar Srivastava (https://samacker77.github.io)
Problem Link - https://www.hackerrank.com/challenges/s10-basic-statistics/problem

Problem Statement - Given an array, X , of N integers, calculate and print the respective mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.
'''


#---------------Solution------------------#

class Solution():
    def __init__(self,X:list,N:int):
        self.X = X
        self.N = N
    def inputs(self):
        return self.X,self.N
    def mean(self):
        return round(sum(self.X)/self.N,1)
    def median(self):
        self.X = sorted(self.X)
        if self.N%2 == 0:
            half = self.N//2
            first_value = self.X[half-1]
            second_value = self.X[half]
            return round((first_value+second_value)/2,2)
        else:
            half = self.N//2
            return self.X[half]
    def mode(self):
        freq = {} #dictionary to store frequencies
        for i in self.X:
            freq[i] = freq.get(i,0)+1
        vals = list(freq.values())
        keys = list(freq.keys())
        return keys[vals.index(max(vals))]
        
            



N = int(input())
X = list(map(int,input().split()))
submit = Solution(X,N)
mean = submit.mean()
median = submit.median()
mode = submit.mode()
print(*[mean,median,mode],sep='\n')

