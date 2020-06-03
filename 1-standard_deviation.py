#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author - Samar Srivastava (https://samacker77.github.io)
Problem Link - https://www.hackerrank.com/challenges/s10-standard-deviation/problem

Problem Statement - Given an array, X , of N integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +/-0.1 will be tolerated for the standard deviation.

'''
#---------------Solution------------------#

class Solution():
    def __init__(self,N:int,X:list):
        self.N = N
        self.X = X
    def inputs(self):
        return self.X, self.N
    def mean(self):
        return sum(self.X)/self.N
    def standard_dev(self,mean:int):
        squared_distance = 0
        for value in self.X:
            squared_distance = squared_distance + (value - mean)**2
        std_dev = (squared_distance/self.N)**0.5
        return std_dev
        




def main():
    N = int(input())
    X = list(map(int,input().split()))
    submit = Solution(N,X)
    mean = submit.mean()
    std_dev = submit.standard_dev(mean)
    print(round(std_dev,1))

if __name__ == '__main__':
    main()


