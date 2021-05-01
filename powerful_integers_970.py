'''
970. Powerful Integers
Medium

Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32

https://leetcode.com/problems/powerful-integers/
'''
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        self.retVal = set()
        self.dfs(x,y,0,0,bound,set()) 
        return list(self.retVal) 
    def dfs(self, x, y, px, py, bound, visited):
        sums = x**px+y**py 
        if sums > bound:
            return 
        if (px,py) in visited:
            return
        visited.add((px,py))
        self.retVal.add(sums)
        if x > 1:
            self.dfs(x,y,px+1, py, bound, visited)
        if y > 1:
            self.dfs(x,y,px, py+1, bound, visited)
        return
