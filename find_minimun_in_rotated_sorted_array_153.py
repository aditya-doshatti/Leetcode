'''
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        i =1
        while i < len(nums):
            if nums[i-1] > nums[i]:
                return nums[i]
            i += 1
        return nums[0]
