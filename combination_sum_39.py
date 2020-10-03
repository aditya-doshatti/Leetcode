'''
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

https://leetcode.com/problems/combination-sum/
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        retVal = []
        self.dfs(candidates, target, [], retVal)
        return retVal
    
    def dfs(self, candidates, target, path, retVal):
        if target < 0:
            return 
        if target == 0:
            retVal.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target-candidates[i], path + [candidates[i]], retVal)
