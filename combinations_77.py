'''
77. Combinations
Medium
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

https://leetcode.com/problems/combinations/
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k==1:
            return [[i] for i in range(1,n+1)]
        elif k==n:
            return [[i for i in range(1,n+1)]]
        else:
            retVal=[]
            retVal+=self.combine(n-1,k)
            tmp=self.combine(n-1,k-1)
            for part in tmp:
                part.append(n)
            retVal+=tmp
        return retVal
        #Brute force TLE
        retVal = []
        def helper(tmp, n, k):
            if n == 0:
                if tmp:
                    a= tmp.pop()
                    while tmp and tmp[-1] <= (k-len(tmp)):
                        a = tmp.pop()
                    helper(tmp, a-1, k)
            else:
                tmp.append(n)
                if len(tmp) == k:
                    retVal.append(tmp[:])
                    tmp.pop()
                helper(tmp, n-1, k)
        helper([], n, k)
        return retVal
