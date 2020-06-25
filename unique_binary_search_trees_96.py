'''
96. Unique Binary Search Trees
Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

https://leetcode.com/problems/unique-binary-search-trees/
'''
class Solution:
    # def __init__(self):
    #     self.lookup ={}

    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]
        # if n == 0 or n == 1:
        #     return 1
        # if n in self.lookup:
        #     return self.lookup[n]
        # retVal = 0
        # for i in range(1, n+1):
        #     retVal += (self.numTrees(i-1) * self.numTrees(n-i))
        # self.lookup[n] = retVal
        # return self.lookup[n]
