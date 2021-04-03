'''
474. Ones and Zeroes
Medium

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

https://leetcode.com/problems/ones-and-zeroes/
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[s.count('0'), s.count('1')] for s in strs]
        @lru_cache(None)
        def dp(i, m, n):
            if i == len(strs):
                return 0
            retVal = dp(i+1, m, n)
            if m >= arr[i][0] and n >= arr[i][1]:
                retVal = max(retVal, dp(i+1, m-arr[i][0], n-arr[i][1]) + 1)
            return retVal
        return dp(0, m, n)
