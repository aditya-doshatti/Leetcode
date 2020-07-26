'''
154. Find Minimum in Rotated Sorted Array II
Hard

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        retVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < retVal:
                retVal = nums[i]
        return retVal
