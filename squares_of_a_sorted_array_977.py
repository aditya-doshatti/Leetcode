'''
977. Squares of a Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

https://leetcode.com/problems/squares-of-a-sorted-array/
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def squared(n):
            return n*n
        for i in range(0, len(nums)):
			# strores the sqared number in the same array
            nums[i] = squared(nums[i])
        return sorted(nums)
        # TLE
        # retVal = []
        # for num in nums:
        #     curr = num ** 2
        #     if len(retVal):
        #         if retVal[-1] <= curr:
        #             retVal.append(curr)
        #         elif retVal[0] >= curr:
        #             retVal.insert(0, curr)
        #         else:
        #             i = 0
        #             while i < len(retVal): # Should do binary search here
        #                 if retVal[i] > curr:
        #                     retVal.insert(i, curr)
        #                     break
        #                 i += 1
        #     else:
        #         retVal.append(curr)
        # return retVal
                    
