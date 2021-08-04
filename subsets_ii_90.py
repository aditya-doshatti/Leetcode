'''
90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

https://leetcode.com/problems/subsets-ii/
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        retVal = []
        for i in range(2**n):
            binrep = bin(i)[2:][::-1]
            # print(binrep)
            curr = []
            for idx,j in enumerate(binrep):
                if j == '1':
                    curr.append(nums[idx])
            # curr.sort()
            if curr not in retVal:
                retVal.append(curr)
            print(retVal)
        return retVal
