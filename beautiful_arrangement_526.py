'''
526. Beautiful Arrangement
Medium

Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

https://leetcode.com/problems/beautiful-arrangement/
'''
class Solution:
    def countArrangement(self, n: int) -> int:
        retVal = 0
        visited = set()
        def dfs(pos=1):
            nonlocal retVal
            if pos > n:
                retVal += 1
                return
            for i in range(1, n + 1): #number 1..n
                if (i not in visited and (pos % i == 0 or i % pos == 0)):
                    visited.add(i)
                    dfs(pos + 1)
                    visited.remove(i)
        dfs()
        return retVal
