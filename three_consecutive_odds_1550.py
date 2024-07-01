'''
1550. Three Consecutive Odds

Easy

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

https://leetcode.com/problems/three-consecutive-odds/description
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        window = 0
        for i in range(min(3, len(arr))):
            window += arr[i] % 2
        if window == 3:
            return True
        for i in range(3, len(arr)):
            window += arr[i] % 2
            window -= arr[i - 3] % 2
            if window == 3:
                return True
        return False
