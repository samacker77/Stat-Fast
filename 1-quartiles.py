#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author - Samar Srivastava (https://samacker77.github.io)
Problem Link - https://www.hackerrank.com/challenges/s10-quartiles/problem

Problem Statement - Given an array, X, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3).
 It is guaranteed that Q1, Q2,and Q3 are integers.
'''


#---------------Solution------------------#

class Solution():
    def __init__(self,N:int,X:list):
        self.N = N
        self.X = X
    def inputs(self):
        return self.N,self.X
    def split_data(self):
        self.X = sorted(self.X)
        if self.N%2 == 0:
            half_ix = self.N//2
            first_half = self.X[:self.N//2]
            second_half = self.X[self.N//2:]
            return first_half, second_half
        else:
            median = self.X[self.N//2]
            first_half = self.X[0:self.N//2]
            second_half = self.X[self.N//2+1:]
            return first_half,second_half
    def median(self,new_X:list):
        new_X = sorted(new_X)
        if len(new_X)%2 == 0:
            ix1 = new_X[len(new_X)//2-1]
            ix2 = new_X[len(new_X)//2]
            return (ix1+ix2)//2
        else:
            return new_X[len(new_X)//2]




def main():
    N = int(input())
    X = list(map(int,input().split()))
    submit = Solution(N,X)
    lower_half,upper_half = submit.split_data()
    Q1 = submit.median(lower_half)
    Q2 = submit.median(X)
    Q3 = submit.median(upper_half)
    print(*[Q1,Q2,Q3],sep='\n')

if __name__ == '__main__':
    main()


