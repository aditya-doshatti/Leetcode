'''
70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

https://leetcode.com/problems/climbing-stairs/
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        def recurse(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in dic:
                return dic[n]

            retVal = recurse(n-1) + recurse(n-2)
            dic[n] = retVal
            return retVal
        return recurse(n)
