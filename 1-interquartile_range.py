#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author - Samar Srivastava (https://samacker77.github.io)
Problem Link - https://www.hackerrank.com/challenges/s10-interquartile-range/problem

Problem Statement - The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e.,Q3-Q1 ).

Given an array,X , of n integers and an array, F , representing the respective frequencies of X's elements,
construct a data set, S, where each x[i] occurs at f[i] frequency .
Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
'''


#---------------Solution------------------#

class Solution():
    def __init__(self,N:int,X:list,F:list):
        self.N = N
        self.X = X
        self.F = F
    def inputs(self):
        return self.N,self.X,self.F
    def unpack_data(self):
        S = []
        for ix in range(len(self.X)):
            for iy in range(self.F[ix]):
                S.append(self.X[ix])
        return S
    def split_data(self,S:list):
        S = sorted(S)
        n = len(S)
        if n%2 == 0:
            half_ix = n//2
            first_half = S[:n//2]
            second_half = S[n//2:]
            return first_half, second_half
        else:
            median = S[n//2]
            first_half = S[0:n//2]
            second_half = S[n//2+1:]
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
    F = list(map(int,input().split()))
    submit = Solution(N,X,F)
    S = submit.unpack_data()
    lower_half,upper_half = submit.split_data(S)
    Q1 = submit.median(lower_half)
    Q3 = submit.median(upper_half)
    interquartile_range = float(Q3-Q1)
    print(round(interquartile_range,1),sep='\n')

if __name__ == '__main__':
    main()


