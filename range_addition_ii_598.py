'''
598. Range Addition II
Easy
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

 

Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

https://leetcode.com/problems/range-addition-ii/
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        xs, ys = defaultdict(int), defaultdict(int)
        for op in ops:
            # print(op, xs, ys)
            for i in range(1, op[0]+1):
                xs[i] += 1
            for j in range(1, op[1]+1):
                ys[j] += 1
        maxX, maxY, maxXval, maxYval = m, n, 0, 0
        # print(xs, ys)
        for k,v in xs.items():
            if v >= maxXval:
                maxX = k
                maxXval = v
        for k,v in ys.items():
            if v >= maxYval:
                maxY = k
                maxYval = v
        return maxX*maxY
