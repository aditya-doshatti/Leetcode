'''
949. Largest Time for Given Digits
Easy

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"

https://leetcode.com/problems/largest-time-for-given-digits/
'''
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        retVal = ''
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    if i == j or i == k or j == k:
                        continue
                    hour, minute = str(a) + str(b), str(c) + str(A[6 - i - j - k])
                    if hour < '24' and minute < '60':
                        print(hour, minute)
                        retVal = max(retVal, hour + ':' + minute)
        return retVal
