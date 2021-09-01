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
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[l] > nums[-1]:
                l = mid+1
            elif mid > 0 and nums[mid] > nums[mid-1]:
                r = mid-1
            else:
                return nums[mid]
