'''
35. Search Insert Position
Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

https://leetcode.com/problems/search-insert-position/
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid
        if l == len(nums) - 1 and target > nums[-1]:
            return len(nums) 
        return l
        # for i,n in enumerate(nums):
        #     if n > target or n == target:
        #         return i
        # return i+1
