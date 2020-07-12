'''
78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

https://leetcode.com/problems/subsets/
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        self.dfs([-1],nums)
        return self.out

    def dfs(self, current, nums):
        self.out.append([nums[s] for s in current][1:])
        for i in range(current[-1] + 1, len(nums)):
            self.dfs(current + [i], nums)
