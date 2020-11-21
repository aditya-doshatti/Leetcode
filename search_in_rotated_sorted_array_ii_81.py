'''
81. Search in Rotated Sorted Array II
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        if nums[0] == nums[-1]:
            return target in  nums
        if nums[1] < nums[0]:
            nums = nums[1:] + [nums[0]]
        l, h = 0, len(nums)-1
        while l <= h:
            print(nums)
            mid = (l+h)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if nums[h] < target and nums[mid] < nums[h]:
                    nums = nums[:mid]
                    l,h = 0,len(nums)-1
                else:
                    l = mid + 1
            elif nums[mid] > target:
                if nums[l] > target:
                    nums = nums[mid+1:]
                    l,h = 0, len(nums)-1
                else:
                    h = mid - 1
        return False
