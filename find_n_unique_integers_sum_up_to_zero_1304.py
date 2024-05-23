'''
1304. Find N Unique Integers Sum up to Zero

Easy

Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        retVal = []
        if n % 2:
            retVal += [0]
        k = n // 2
        while k:
            retVal += [k]
            retVal += [-1 * k]
            k -= 1
        return retVal
