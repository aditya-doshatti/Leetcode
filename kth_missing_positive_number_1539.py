'''
1539. Kth Missing Positive Number
Easy

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

https://leetcode.com/problems/kth-missing-positive-number/
'''
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arrSet = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arrSet:
                k -= 1
            if k == 0:
                return i
