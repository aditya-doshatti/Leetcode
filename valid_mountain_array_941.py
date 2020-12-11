'''
941. Valid Mountain Array
Easy

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false

https://leetcode.com/problems/valid-mountain-array/
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        flag, i, peak = arr[0] < arr[1],1, 0
        while i < len(arr):
            if flag and arr[i-1] > arr[i]:
                peak += 1
                flag = False
            if not flag and arr[i-1] <= arr[i]:
                return False
            i += 1
        return peak == 1
